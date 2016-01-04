#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication)
import RPi.GPIO as GPIO
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

# class mainApp(QMainWindow, Ui_MainWindow):
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(277, 310)
        self.buttonOn = QtWidgets.QPushButton(Form)
        self.buttonOn.setGeometry(QtCore.QRect(90, 80, 98, 27))
        self.buttonOn.setObjectName(_fromUtf8("buttonOn"))
        self.buttonOff = QtWidgets.QPushButton(Form)
        self.buttonOff.setGeometry(QtCore.QRect(90, 170, 98, 27))
        self.buttonOff.setObjectName(_fromUtf8("buttonOff"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.buttonOn.setText(_translate("Form", "On", None))
        self.buttonOff.setText(_translate("Form", "Off", None))
        self.buttonOn.clicked.connect(self.ledOn)
        self.buttonOff.clicked.connect(self.ledOff)

    def ledOn (self):
        GPIO.setmode(GPIO.BOARD)
        led = 37
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, 1)
        GPIO.cleanup

    def ledOff (self):
        GPIO.setmode(GPIO.BOARD)
        led = 37
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, 0)
        GPIO.cleanup

# if __name__ == "__main__":
#    import sys

#    app = QtWidgets.QApplication(sys.argv)
#    Form = QtGui.QWidget()
#    ui = Ui_Form()
#    ui.setupUi(Form)
#    Form.show()
#    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Form()
    Ui_Form.show()
    sys.exit(app.exec_())