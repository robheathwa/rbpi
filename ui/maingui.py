# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maingui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 110, 91, 16))
        self.label.setObjectName("label")
        self.buttonOn = QtWidgets.QPushButton(self.centralwidget)
        self.buttonOn.setGeometry(QtCore.QRect(200, 150, 113, 32))
        self.buttonOn.setObjectName("buttonOn")
        self.buttonQuit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonQuit.setGeometry(QtCore.QRect(310, 220, 113, 32))
        self.buttonQuit.setObjectName("buttonQuit")
        self.buttonOff = QtWidgets.QPushButton(self.centralwidget)
        self.buttonOff.setGeometry(QtCore.QRect(200, 180, 113, 32))
        self.buttonOff.setObjectName("buttonOff")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.buttonQuit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "LED Switch"))
        self.buttonOn.setText(_translate("MainWindow", "LED ON"))
        self.buttonQuit.setText(_translate("MainWindow", "Quit"))
        self.buttonOff.setText(_translate("MainWindow", "LED OFF"))

