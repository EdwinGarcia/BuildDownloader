from tkinter import *
import tkinter
top = tkinter.Tk()

#label for the version select box
versionLabel = Label(top, text="Select Version:")
#scrollbar widget for version list
scrollbar = Scrollbar(top)
scrollbar.pack( side = RIGHT, fill=Y )

#version listbox widget
#todo: come up with a way to poll for all packes on FTP
Lb1 = Listbox(top, selectmode="extended", height=3, yscrollcommand=scrollbar.set)
Lb1.insert(1, "3.2")
Lb1.insert(2, "3.0.3")
Lb1.insert(3, "2.2.2")
Lb1.insert(4, "2.1")
Lb1.insert(5, "256->512MB bootloader")
Lb1.insert(6, "1.3.4")

#drop down list of attached USB drives to save build to.

'''
def SaveLocation():
	
def FTPshit():
'''

#button widget
#insert a command = ftpCallBack
D = tkinter.Button(text="Download")

#activates the widgets
versionLabel.pack()
Lb1.pack()
D.pack()
top.mainloop()