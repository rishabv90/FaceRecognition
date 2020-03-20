# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\risha\OneDrive\Desktop\faceRecGui\guiTest\guitTest1\page1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!



from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QPixmap 
import sys 
#from page2 import Ui_MainWindow2
#from page3 import Ui_MainWindow3
#import page2
#import page3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 732)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 310, 281, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 430, 281, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 90, 221, 161))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 21))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #button links
        self.pushButton.clicked.connect(self.goToPage2)
        self.pushButton_2.clicked.connect(self.goToPage3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Manual Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Facial Recognition"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"Webp.net-resizeimage.jpg\"/></p></body></html>")) ## change directory to roche image
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))

    def goToPage2(self): #close current window, create new object of new window, open new window
       # MainWindow.close()
        print("Manual Login Clicked")
        self.window = QtWidgets.QMainWindow()
        self.ui =  page2.Ui_MainWindow2()
        self.ui.setupUi(self.window)
        self.window.show()


    def goToPage3(self):
        MainWindow.close()
        print("Face Rec Login Clicked")
        self.window = QtWidgets.QMainWindow()
        self.ui =  page3.Ui_MainWindow3()
        self.ui.setupUi(self.window)
        self.window.show()
        
   

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
