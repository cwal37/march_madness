# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 15:24:01 2016

@author: wal

tutorial:
http://www.learningpython.com/2008/09/20/an-introduction-to-pyqt/
"""

import PyQt4
import sys
from PyQt4 import QtGui

class HelloWindow(QtGui.QMainWindow):

	def __init__(self, win_parent = None):
		#Init the base class
		QtGui.QMainWindow.__init__(self, win_parent)
		self.create_widgets()

	def create_widgets(self):
		#Widgets
		self.label = QtGui.QLabel("Say hello:")
		self.hello_edit = QtGui.QLineEdit()
		self.hello_button = QtGui.QPushButton("Push Me!")
		#Horizontal layout
		h_box = QtGui.QHBoxLayout()
		h_box.addWidget(self.label)
		h_box.addWidget(self.hello_edit)
		h_box.addWidget(self.hello_button)
		#Create central widget, add layout and set
		central_widget = QtGui.QWidget()
		central_widget.setLayout(h_box)
		self.setCentralWidget(central_widget)

if __name__ == "__main__":
	# Someone is launching this directly
	# Create the QApplication
	app = QtGui.QApplication(sys.argv)
	#The Main window
	main_window = HelloWindow()
	main_window.show()
	# Enter the main loop
	app.exec_()
