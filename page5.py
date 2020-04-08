
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\risha\OneDrive\Desktop\faceRecGui\guiTest\guitTest1\page7_update.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
# After admin logged in 

from PySide2 import QtCore, QtGui, QtWidgets
from datetime import *
import asyncio, io, glob, os, sys, time, uuid, requests, cv2
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType
import page1, page4
global KEY
# Set the FACE_SUBSCRIPTION_KEY environment variable with your key as the value.
# This key will serve all examples in this document.
#KEY = os.environ['FACE_SUBSCRIPTION_KEY']
KEY = '12f952f3b226421aa2019ab14740b123'

# Set the FACE_ENDPOINT environment variable with the endpoint from your Face service in Azure.
# This endpoint will be used in all examples in this quickstart.
global ENDPOINT
ENDPOINT = "https://testface19025.cognitiveservices.azure.com"



global face_client
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

 
# Used in the Person Group Operations,  Snapshot Operations, and Delete Person Group examples.
# You can call list_person_groups to print a list of preexisting PersonGroups.
# SOURCE_PERSON_GROUP_ID should be all lowercase and alphanumeric. For example, 'mygroupname' (dashes are OK).
global PERSON_GROUP_ID
PERSON_GROUP_ID = 'test'

global path
path = "/Users/Julia/source/repos/updateGUI/"

class Ui_MainWindow(object):
    def __init__(self, name):
        self._name = name

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1136, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #PUSH BUTTONS
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(920, 780, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 730, 151, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(780, 460, 151, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(730, 780, 151, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        #RADIO BUTTONS
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(870, 390, 101, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(1000, 390, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        #USER INPUTS
        #Name
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(870, 260, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        #Username
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(870, 300, 221, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        #Password
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setGeometry(QtCore.QRect(870, 340, 221, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
      
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(20, 690, 611, 20))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 660, 61))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1000, 10, 111, 51))
        self.label_8.setStyleSheet("image: url(samPicture.jpg);")
        self.label_8.setText("")
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setPixmap(QtGui.QPixmap("samPicture.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(670, 240, 221, 61))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(670, 280, 221, 61))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(670, 320, 221, 61))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(670, 370, 221, 61))
        self.label_12.setObjectName("label_12")
        

        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(20, 160, 631, 551))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setColumnCount(5)
        self.treeWidget.setHeaderLabels(["Name",'Account Type', 'Login time', 'Logout time', 'Date'])
        person_groups = face_client.person_group.list(start=None, top=1000, return_recognition_model=False, custom_headers=None, raw=False)
        dic = {}

        for PersonGroupObj in person_groups:
            dic[PersonGroupObj.name] = []
            people = face_client.person_group_person.list(PersonGroupObj.name, start=None, top=None, custom_headers=None, raw=False)
            for p in people:
                print('DATA::::::::::::::::::: ' + p.user_data)

                data = p.user_data.split(',')
                print(data)
                dic[PersonGroupObj.name].append([p.name,data[0],data[1],data[2],data[3],data[4],data[5]])
        keys= list(dic.keys())

       
        for i in range(0,len(dic[keys[0]])):
            print(type(i))
            row = QtWidgets.QTreeWidgetItem(self.treeWidget)
            row.setText(0,dic[keys[0]][i][0])
            row.setText(1,dic[keys[0]][i][4])
            row.setText(2,dic[keys[0]][i][2])
            row.setText(3,dic[keys[0]][i][3])
            row.setText(4,dic[keys[0]][i][1])

           

        print(dic)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(630, 160, 20, 551))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1136, 21))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuExit.menuAction())

        self.pushButton_5.clicked.connect(self.goAddUser)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Logout"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete"))
        self.pushButton_4.setText(_translate("MainWindow", "Modify"))
        self.radioButton.setText(_translate("MainWindow", "Administravtive"))
        self.radioButton_2.setText(_translate("MainWindow", "Regular User"))
        self.pushButton_5.setText(_translate("MainWindow", "Create new User"))
        #self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Adminstrative Functions</span></p></body></html>"))
        self.label_7.setStyleSheet(_translate("MainWindow", "font-size:24pt; font-weight:600;"))
        self.label_7.setText(_translate("MainWindow", "Adminstrator "+ self._name + "'s Functions Page"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter new name :</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter new username :</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter new password :</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter new status :</span></p></body></html>"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))

    def goAddUser(self):
        MainWindow.hide()
        print("Go to manual login page")
        self.window = QtWidgets.QMainWindow()
        self.ui = page4.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        return 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow("Empty")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
