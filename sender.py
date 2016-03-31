import serial
import re
import wx
import senderGUI
import time
import threading
import  wx.lib.newevent
terminator = '\r\n'



doColor = True

updateEvent, EVT_UPDATE = wx.lib.newevent.NewEvent()
doneEvent, EVT_DONE = wx.lib.newevent.NewEvent()
penChangeEvent, EVT_PENCHANGE = wx.lib.newevent.NewEvent()
comEvent, EVT_COM = wx.lib.newevent.NewEvent()


class Sender (threading.Thread):
	def __init__(self, parent) :
		threading.Thread.__init__(self)
		try :
			self.port = serial.Serial('/dev/ttyUSB0', 57600, timeout=.5)
			
		except :
			pass
			
		self.data = ''
		self.line = ''
		self.baudRates = [300, 1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600, 115200]
		self.lines = ''
		self.parent = parent			
		self.keepAlive = True
		self.pauseFlag = False
		self.servoPosition = 15		
		self.running = False
		self.verbosity = 1
	

	def isRunning(self) :
		return self.running
		
	def moveAngle(self, amount) :
		self.send('G91\n')
		self.send('G0 X' + str(amount) + '\n')
		self.send('G90')
		
	def moveRotation(self, amount) :
		self.send('G91\n')
		self.send('G0 Y' + str(amount) + '\n')
		self.send('G90')
		
	def moveServo(self, position) :
		self.send('M300 S' + str(position) + '\n')
	
		
	def flush(self) :
		self.port.flush()
		self.port.flushInput()		

		
	def openPort(self, port, baud):
		self.port = serial.Serial(port, baud, timeout=0.5)
		time.sleep(1)
		self.port.flushInput()
		time.sleep(.5)
		if self.verbosity > 0 : print "Port opened and ready!"
		
		
		
	def run(self) :	
		global buff		
		totalLines = self.parent.richText.GetNumberOfLines()
		
		text = self.parent.richText.GetValue()
		
		lines = text.split('\n')
		self.parent.richText.Clear()
		lineCounter = 0
		self.running = True
		
		if self.verbosity > 0 :
			print "Started sender thread..."

		for line in lines :
			try :			
					
				self.line = line
				
				if self.verbosity > 1 :
					print 'Line Read from file: ', self.line
				
				if not self.keepAlive :
					linecounter = 0
					break					
				
				
				try :
					if 'M01' in self.line and (self.parent.doPenChange_Checkbox.GetValue() == True):
						gcode, msgText = line.split('(')
						msgText = msgText.strip(')')
						self.pauseFlag = True
						evt = penChangeEvent(attr1=msgText)
						wx.PostEvent(self.parent, evt)
				except Exception, detail :
					print "ERROR looking for pen change!\n" + str(detail)
					
					
				while self.pauseFlag :		# Hang here in sleep until program resumes...
					time.sleep(.1)					
				
				if '(' in self.line or ')' in self.line :
					self.line = self.strip(self.line)
					
				if (self.parent.servoOff_Checkbox.GetValue() == True) and ('M300 S255' in self.line) :
					if self.verbosity > 1 :
						print '++++ Removing  Servo off command'
					self.line = ''
					
				try :
					if len(self.line) > 1 :	
						if self.verbosity > 2 : print "Sending: " + str(line)
							
						self.send(self.line)				
				
					else :
						if self.verbosity > 1 :
							print 'Skipping empty line'
							
						else :
							pass			
				except Exception, detail :
					print "ERROR sending data: " + str(detail)
				
				if  self.parent.colorize_Checkbox.GetValue() == True : time.sleep(0.1)
				evt = updateEvent(attr1=line)
				wx.PostEvent(self.parent, evt)					
				
			except Exception, detail:
				print "ERROR! UNHANDLED EXCEPTION: " + str(detail)
		
		time.sleep(.1)
		self.parent.richText.Clear()
		time.sleep(.1)
		self.parent.richText.AppendText(text)
		self.running = False
		self.parent.run_Button.Enable(True)
				
		
	def strip(self, line) :	
		regex = re.compile('\(.+?\)')
		out = regex.sub('', line)
		return out
		
	def send(self, code) :	
		
		if not terminator in code :
			code += terminator
		try :
			if self.verbosity > 2 : print "+++ sending to port ---->" + code
			self.port.write(str(code))
			
		except Exception, detail : 
			print "Error writing port: " + str(detail)
		returned = ''
		count = 0
		while True :
			if self.verbosity > 1 :
				print 'polling :', count
			
			returned = self.port.readline().strip('\r\n')
			
			if self.verbosity > 1 :
				print "Read from 'bot: ", returned
			if returned == 'ok ' + code.strip('\r\n') :	
				break
			count += 1


	

class GUI (senderGUI.mainFrame):
	def __init__ (self, parent):		
		senderGUI.mainFrame.__init__(self, parent)
		self.sender = Sender(self)
		self.fileName = ''
		self.contents = ''
		self.Bind(EVT_UPDATE, self.onUpdate)
		self.Bind(EVT_PENCHANGE, self.onPenChange)		
		self.ports = self.findPorts()
		self.updatePorts(self.ports)
		self.penPosition_Label.SetLabel(str(self.sender.servoPosition))
		self.counter = 1
		self.thread = threading.Thread()
		
		TIMER_ID = 100  
		self.timer = wx.Timer(self, TIMER_ID)  
		
		wx.EVT_TIMER(self, TIMER_ID, self.onTimer)  
		self.Bind(wx.EVT_CLOSE, self.onClose)
		

	def onClose(self, event) :
		self.sender.keepAlive = False
		try :
			self.sender.port.close()
		except :
			pass
		
		try :
			self.f.close()
		except :
			pass	
		
		self.Destroy()
			
	
	def onTimer(self, event) :		
		global doColor
		global buff
		for i in range(0, len(buff)) :
			line = buff.pop(0)			
			if '(' in line and doColor:	
				line += '\n'
				for letter in line :
					if letter == '(' :
						print 'Start..'
						self.richText.BeginTextColour(wx.BLUE)
					if letter == ')' :
						print 'Stop!'
						self.richText.EndTextColour()	
					print letter	
													
					self.richText.WriteText(letter) 	
			else :				
				self.richText.AppendText(line + '\n')
			
		self.richText.ShowPosition(self.richText.GetLastPosition ())		
		self.counter += 1
		

	def onClear (self, event) :
		self.richText.Clear()

	def onDone(self, event) :
		self.run_Button.Enable()
		
	def updatePorts(self, portsList) :	
		self.serPort_Choice.Clear()	
		for i in portsList :
			self.serPort_Choice.Append(i)
		self.serPort_Choice.SetSelection(0)
			
	def findPorts(self) :  
		ports = []
		for i in range(64) :  #  Windows
			try :                
				s = serial.Serial("COM" + str(i))                
				s.close()
				ports.append("COM" + str(i))                
			except :
				pass
				
		if len(ports) > 0 : 
			return ports

		for i in range(64) :
			for k in ["/dev/ttyUSB", "/dev/ttyACM", "/dev/ttyS"] : # Linux
				try :		
					s = serial.Serial(k+str(i))
					s.close()                
					ports.append(k+ str(i))					 

				except :
					pass	
		
		return ports
		
	def onRescan(self, event) :
		self.ports = self.findPorts()
		self.updatePorts(self.ports)
		pass	
        
	def onUpdate(self, event)	:
		event.attr1 += '\n'
		killColor = False
		
		if self.colorize_Checkbox.GetValue() == True :
			if '(' in event.attr1 :
				for letter in event.attr1 :
					if letter == '(' :										
						self.richText.BeginTextColour(wx.BLUE)	
						killColor = False				
							
					elif letter == ')' :		
						killColor = True	
						
					self.richText.WriteText(letter) 			
					if killColor :
						self.richText.EndTextColour()	
						killColor = False								
						
			if 'G1' in event.attr1 :
				self.richText.BeginTextColour(wx.GREEN)	
				self.richText.WriteText(event.attr1) 
				self.richText.EndTextColour()			
			
				
		else :	
			self.richText.AppendText(event.attr1)
			
		self.richText.ShowPosition(self.richText.GetLastPosition ())		
		self.counter += 1
		
	def onFileSelection(self, event) :
		self.richText.Clear()
		self.fileName = self.filePicker.GetPath()
		self.f = open(self.fileName, 'r')
		self.contents = self.f.readlines()
		for line in self.contents :		
			self.richText.AppendText(line)
			
	def onRun(self, event) :	
		try :
			del self.sender
		except :
			print "Can't KEEEEEEL it!"
			
		self.run_Button.Enable(False) 
		self.sender = Sender(self)
		
		self.onSerPortOpen(None)

		try :
			assert self.sender.port.isOpen()			
		except :
			print 'Error:   Port not open!'
			return
			
		self.sender.keepAlive = True				
		self.thread = threading.Thread(target=self.sender)
		#self.thread.daemon = True
		self.thread = self.sender.start()	


		
	def onStop(self, event) :
		self.sender.keepAlive = False
		self.timer.Stop()
		self.pause_Button.SetValue(False)
		self.run_Button.Enable(True) 
		
		
	def onSerPortOpen(self, event) :

		port = self.ports[self.serPort_Choice.GetSelection()]
		baud = self.sender.baudRates[self.baud_Choice.GetSelection()]
		self.sender.openPort(port, baud)
		print self.sender.port
		self.sender.moveServo(self.sender.servoPosition)	

	def onPenChange(self, event) :
		dlgText = event.attr1 	 + "\nInsert correct pen and press 'OK' to continue"		
		dlg = wx.MessageDialog(None, dlgText, 'Pen Change!', wx.OK | wx.ICON_EXCLAMATION)
		dlg.ShowModal()
		self.sender.pauseFlag = False

		
	def onPenPlus(self, event) :
		
		self.sender.servoPosition -= int(self.degrees_TextCtrl.GetValue())
		if self.sender.servoPosition < 0 : self.sender.servoPosition = 0
		self.sender.moveServo(self.sender.servoPosition)
		self.penPosition_Label.SetLabel(str(self.sender.servoPosition))
		
	def onPenMinus(self, event) :
		self.sender.servoPosition += int(self.degrees_TextCtrl.GetValue())
		if self.sender.servoPosition > 90 : self.sender.servoPosition = 90
		self.sender.moveServo(self.sender.servoPosition)
		self.penPosition_Label.SetLabel(str(self.sender.servoPosition))

	def onPause(self, event) :
		if self.pause_Button.GetValue() == True :
			self.sender.pauseFlag = True
		
		else :
			self.sender.pauseFlag = False

		
	def onAngleRight(self, event) :
		self.sender.moveAngle(float(self.angleMM_TextCtrl.GetValue()) )
		
	def onAngleLeft(self, event) :
		self.sender.moveAngle(float(self.angleMM_TextCtrl.GetValue()) * -1 )
		

	def onRotPlus(self, event) :
		self.sender.moveRotation(float(self.rotationMM_TextCtrl.GetValue()) * -1)
		
		
	def onRotMinus(self, event) :
		self.sender.moveRotation(float(self.rotationMM_TextCtrl.GetValue()))
		
	

if __name__ == '__main__':
    app = wx.App(0)
    frame = GUI(None)
    frame.Show()
    app.MainLoop()
	
