# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 650,768 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		masterSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.masterPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		panelSizer = wx.BoxSizer( wx.VERTICAL )
		
		fileNameSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.fileName_Label = wx.StaticText( self.masterPanel, wx.ID_ANY, u"GCode File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fileName_Label.Wrap( -1 )
		fileNameSizer.Add( self.fileName_Label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.filePicker = wx.FilePickerCtrl( self.masterPanel, wx.ID_ANY, u"/home/jesse/AutoSave_Untitled.skp", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.filePicker.SetMinSize( wx.Size( 300,-1 ) )
		
		fileNameSizer.Add( self.filePicker, 0, wx.ALL, 5 )
		
		
		panelSizer.Add( fileNameSizer, 0, wx.EXPAND, 5 )
		
		serPortSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.serPort_Label = wx.StaticText( self.masterPanel, wx.ID_ANY, u"Serial Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.serPort_Label.Wrap( -1 )
		serPortSizer.Add( self.serPort_Label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		serPort_ChoiceChoices = []
		self.serPort_Choice = wx.Choice( self.masterPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, serPort_ChoiceChoices, 0 )
		self.serPort_Choice.SetSelection( 0 )
		serPortSizer.Add( self.serPort_Choice, 0, wx.ALL, 5 )
		
		self.serPortRescan_Button = wx.Button( self.masterPanel, wx.ID_ANY, u"Rescan", wx.DefaultPosition, wx.DefaultSize, 0 )
		serPortSizer.Add( self.serPortRescan_Button, 0, wx.ALL, 5 )
		
		
		serPortSizer.AddSpacer( ( 50, 0), 0, wx.EXPAND, 5 )
		
		self.baud_Label = wx.StaticText( self.masterPanel, wx.ID_ANY, u"Baud Rate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.baud_Label.Wrap( -1 )
		serPortSizer.Add( self.baud_Label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		baud_ChoiceChoices = [ u"300", u"1200", u"2400", u"4800", u"9600", u"14400", u"19200", u"28800", u"38400", u"57600", u"115200" ]
		self.baud_Choice = wx.Choice( self.masterPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, baud_ChoiceChoices, 0 )
		self.baud_Choice.SetSelection( 9 )
		serPortSizer.Add( self.baud_Choice, 0, wx.ALL, 5 )
		
		self.serPortOpen_button = wx.Button( self.masterPanel, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		serPortSizer.Add( self.serPortOpen_button, 0, wx.ALL, 5 )
		
		
		panelSizer.Add( serPortSizer, 0, wx.EXPAND, 5 )
		
		jogSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline2 = wx.StaticLine( self.masterPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		jogSizer.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		jogGridSizer = wx.GridSizer( 4, 10, 0, 0 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.penPlus_Button = wx.Button( self.masterPanel, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		jogGridSizer.Add( self.penPlus_Button, 0, wx.ALL, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.rotationPlus_Button = wx.Button( self.masterPanel, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		jogGridSizer.Add( self.rotationPlus_Button, 0, wx.ALL, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.penPosition_Label = wx.StaticText( self.masterPanel, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.penPosition_Label.Wrap( -1 )
		jogGridSizer.Add( self.penPosition_Label, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.penText_Label = wx.StaticText( self.masterPanel, wx.ID_ANY, u"Pen", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.penText_Label.Wrap( -1 )
		jogGridSizer.Add( self.penText_Label, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.angleLeft_Button = wx.Button( self.masterPanel, wx.ID_ANY, u"<=", wx.DefaultPosition, wx.DefaultSize, 0 )
		jogGridSizer.Add( self.angleLeft_Button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self.masterPanel, wx.ID_ANY, u"Angle", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		jogGridSizer.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.angleRight_Button = wx.Button( self.masterPanel, wx.ID_ANY, u"=>", wx.DefaultPosition, wx.DefaultSize, 0 )
		jogGridSizer.Add( self.angleRight_Button, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.rotation_Label = wx.StaticText( self.masterPanel, wx.ID_ANY, u"Rotation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rotation_Label.Wrap( -1 )
		jogGridSizer.Add( self.rotation_Label, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.penMinus_Button = wx.Button( self.masterPanel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		jogGridSizer.Add( self.penMinus_Button, 0, wx.ALL, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.rotationMinus_Button = wx.Button( self.masterPanel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		jogGridSizer.Add( self.rotationMinus_Button, 0, wx.ALL, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.degrees_Label = wx.StaticText( self.masterPanel, wx.ID_ANY, u"Degrees", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.degrees_Label.Wrap( -1 )
		jogGridSizer.Add( self.degrees_Label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.degrees_TextCtrl = wx.TextCtrl( self.masterPanel, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		jogGridSizer.Add( self.degrees_TextCtrl, 0, wx.ALL, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.angleMM_Label = wx.StaticText( self.masterPanel, wx.ID_ANY, u"MM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.angleMM_Label.Wrap( -1 )
		jogGridSizer.Add( self.angleMM_Label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.angleMM_TextCtrl = wx.TextCtrl( self.masterPanel, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		jogGridSizer.Add( self.angleMM_TextCtrl, 0, wx.ALL, 5 )
		
		
		jogGridSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.rotationMM_Label = wx.StaticText( self.masterPanel, wx.ID_ANY, u"MM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rotationMM_Label.Wrap( -1 )
		jogGridSizer.Add( self.rotationMM_Label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.rotationMM_TextCtrl = wx.TextCtrl( self.masterPanel, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		jogGridSizer.Add( self.rotationMM_TextCtrl, 0, wx.ALL, 5 )
		
		
		jogSizer.Add( jogGridSizer, 1, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.masterPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		jogSizer.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		panelSizer.Add( jogSizer, 0, wx.EXPAND, 5 )
		
		fileOpsSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.run_Button = wx.Button( self.masterPanel, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
		fileOpsSizer.Add( self.run_Button, 0, wx.ALL, 5 )
		
		
		fileOpsSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.pause_Button = wx.ToggleButton( self.masterPanel, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.DefaultSize, 0 )
		fileOpsSizer.Add( self.pause_Button, 0, wx.ALL, 5 )
		
		
		fileOpsSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.stop_Button = wx.Button( self.masterPanel, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		fileOpsSizer.Add( self.stop_Button, 0, wx.ALL, 5 )
		
		
		panelSizer.Add( fileOpsSizer, 0, wx.EXPAND, 5 )
		
		functionalSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.servoOff_Checkbox = wx.CheckBox( self.masterPanel, wx.ID_ANY, u"Suppress Servo Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.servoOff_Checkbox.SetValue(True) 
		functionalSizer.Add( self.servoOff_Checkbox, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
		
		self.doPenChange_Checkbox = wx.CheckBox( self.masterPanel, wx.ID_ANY, u"Pen Change on M01", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.doPenChange_Checkbox.SetValue(True) 
		functionalSizer.Add( self.doPenChange_Checkbox, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
		
		self.colorize_Checkbox = wx.CheckBox( self.masterPanel, wx.ID_ANY, u"Colorize text (slower print)", wx.DefaultPosition, wx.DefaultSize, 0 )
		functionalSizer.Add( self.colorize_Checkbox, 0, wx.ALL, 5 )
		
		
		panelSizer.Add( functionalSizer, 0, wx.ALIGN_LEFT|wx.EXPAND, 5 )
		
		textBoxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.richText = wx.richtext.RichTextCtrl( self.masterPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		textBoxSizer.Add( self.richText, 1, wx.EXPAND |wx.ALL, 5 )
		
		clearButtonSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		
		clearButtonSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.clear_Button = wx.Button( self.masterPanel, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		clearButtonSizer.Add( self.clear_Button, 0, wx.ALL, 5 )
		
		
		clearButtonSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		textBoxSizer.Add( clearButtonSizer, 0, wx.EXPAND, 5 )
		
		
		panelSizer.Add( textBoxSizer, 2, wx.EXPAND, 5 )
		
		
		self.masterPanel.SetSizer( panelSizer )
		self.masterPanel.Layout()
		panelSizer.Fit( self.masterPanel )
		masterSizer.Add( self.masterPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( masterSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.onFileSelection )
		self.serPort_Choice.Bind( wx.EVT_CHOICE, self.onSerportChoice )
		self.serPortRescan_Button.Bind( wx.EVT_BUTTON, self.onRescan )
		self.serPortOpen_button.Bind( wx.EVT_BUTTON, self.onSerPortOpen )
		self.penPlus_Button.Bind( wx.EVT_BUTTON, self.onPenPlus )
		self.rotationPlus_Button.Bind( wx.EVT_BUTTON, self.onRotPlus )
		self.angleLeft_Button.Bind( wx.EVT_BUTTON, self.onAngleLeft )
		self.angleRight_Button.Bind( wx.EVT_BUTTON, self.onAngleRight )
		self.penMinus_Button.Bind( wx.EVT_BUTTON, self.onPenMinus )
		self.rotationMinus_Button.Bind( wx.EVT_BUTTON, self.onRotMinus )
		self.run_Button.Bind( wx.EVT_BUTTON, self.onRun )
		self.pause_Button.Bind( wx.EVT_TOGGLEBUTTON, self.onPause )
		self.stop_Button.Bind( wx.EVT_BUTTON, self.onStop )
		self.clear_Button.Bind( wx.EVT_BUTTON, self.onClear )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onFileSelection( self, event ):
		event.Skip()
	
	def onSerportChoice( self, event ):
		event.Skip()
	
	def onRescan( self, event ):
		event.Skip()
	
	def onSerPortOpen( self, event ):
		event.Skip()
	
	def onPenPlus( self, event ):
		event.Skip()
	
	def onRotPlus( self, event ):
		event.Skip()
	
	def onAngleLeft( self, event ):
		event.Skip()
	
	def onAngleRight( self, event ):
		event.Skip()
	
	def onPenMinus( self, event ):
		event.Skip()
	
	def onRotMinus( self, event ):
		event.Skip()
	
	def onRun( self, event ):
		event.Skip()
	
	def onPause( self, event ):
		event.Skip()
	
	def onStop( self, event ):
		event.Skip()
	
	def onClear( self, event ):
		event.Skip()
	

