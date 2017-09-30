# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findWords.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 401)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 70, 551, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.wordsSearched = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.wordsSearched.setObjectName("wordsSearched")
        self.gridLayout.addWidget(self.wordsSearched, 0, 0, 1, 2)
        self.siteURL = QtWidgets.QLineEdit(self.centralwidget)
        self.siteURL.setGeometry(QtCore.QRect(100, 20, 349, 32))
        self.siteURL.setObjectName("siteURL")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 91, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btFindWords = QtWidgets.QPushButton(self.centralwidget)
        self.btFindWords.setGeometry(QtCore.QRect(470, 20, 88, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btFindWords.setFont(font)
        self.btFindWords.setObjectName("btFindWords")
        ##### Button Event ########
        self.btFindWords.clicked.connect(self.clickMethod)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.connect(self.btFindWords, SIGNAL("clicked()"), userFindWords.findAllWords(userSiteUrl))

    def clickMethod(self):
    	    print(self.siteURL.text())
    	    browser = webdriver.Firefox()
    	    browser.get("https://"+self.siteURL.text())
    	    time.sleep(10)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FindWords"))
        self.label.setText(_translate("MainWindow", "Site URL:"))
        self.btFindWords.setText(_translate("MainWindow", "Find Words"))

        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
