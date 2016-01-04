#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'heath'

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.maingui import Ui_MainWindow
import RPi.GPIO as GPIO

# Global Settings
# QApplication.setStyle("cleanlooks")  # set application style

# Main Application Class


class mainApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(mainApp, self).__init__(parent)
        self.setupUi(self)

# Main GUI Code
#    Button Actions
        self.buttonOn.clicked.connect(self.ledOn)
        self.buttonOff.clicked.connect(self.ledOff)

# Classes and Definitions

    def ledOn (self):
#        GPIO.setmode(GPIO.BOARD)
        led = 18
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.HIGH)
#        GPIO.cleanup

    def ledOff(self):
#        GPIO.setmode(GPIO.BOARD)
        led = 18
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.LOW)
#        GPIO.cleanup

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = mainApp()
    window.show()
    sys.exit(app.exec_())
