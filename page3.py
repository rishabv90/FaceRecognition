  
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\risha\OneDrive\Desktop\faceRecGui\guiTest\guitTest1\page4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
# Normal user's logged in successfully page

#from PySide2 import QtCore, QtGui, QtWidgets
from PySide2 import QtCore, QtGui, QtWidgets
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType
from datetime import *
import time
global KEY
KEY = '12f952f3b226421aa2019ab14740b123'

# Set the FACE_ENDPOINT environment variable with the endpoint from your Face service in Azure.
# This endpoint will be used in all examples in this quickstart.
global ENDPOINT
ENDPOINT = "https://testface19025.cognitiveservices.azure.com"

global PERSON_GROUP_ID
PERSON_GROUP_ID = 'test'

global face_client
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

import page1

class Ui_MainWindow(object):
    def __init__(self, name, personID):
        self._name = name 
        self._person_id = personID

    def setupUi(self, MainWindow):
        self.w = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1138, 902)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 620, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 310, 681, 191))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 580, 61))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1000, 10, 111, 51))
        self.label_5.setStyleSheet("image: url(samPicture.jpg);")
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setPixmap(QtGui.QPixmap("samPicture.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1138, 21))
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
        self.pushButton_2.clicked.connect(self.goToPage1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Logout"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Thank you for logging in. Please Logout when you are done. </span></p></body></html>"))
        #self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Normal User Logged in Page</span></p></body></html>"))
        self.label_4.setStyleSheet(_translate("MainWindow", "font-size:24pt; font-weight:600;"))
        self.label_4.setText(_translate("MainWindow", "Normal User - " + self._name + "'s Page"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))

    def goToPage1(self):#logout button
        person = face_client.person_group_person.get('test',self._person_id)
        data = person.user_data.split(',')
        print(data)

        newData = data[0] +','+ data[1] +  datetime.now().strftime(',%H:%M:%S,')  + data[-3] + ',' + data[-2] + ',' + data[-1]
        print(newData)      
        face_client.person_group_person.update(PERSON_GROUP_ID,self._person_id,user_data = newData)

        self.w.hide()
        print("go back to main page")
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui =  page1.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow("EmptyName", "Person_ID")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
