
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\risha\OneDrive\Desktop\faceRecGui\guiTest\guitTest1\page7_update.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
# After admin logged in 

#from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2 import QtCore, QtGui, QtWidgets
from datetime import *
from threading import Timer
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
path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
path = path.replace('C:','')
path = path.replace('\\','/')
path = path + '/'

class Ui_MainWindow(object):
    def __init__(self, name, personID):
        self._name = name
        self._person_id = personID
       

    def setupUi(self, MainWindow):
        self.w = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1136, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #PUSH BUTTONS
        #loggout
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(920, 780, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        #delete
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 730, 151, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        #modify
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(780, 460, 151, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        #new user button
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
      
        self.updateTable()
           

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

        self.pushButton_2.clicked.connect(self.loggout)
        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton_5.clicked.connect(self.goAddUser)
        self.pushButton_4.clicked.connect(self.modify)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.timer = QtCore.QTimer(self.centralwidget)
        self.timer.setSingleShot(False)
        self.timer.setInterval(1)
        self.timer.start()
        self.timer.timeout.connect(self.disableTyping)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Users List"))
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
        
    def disableTyping(self):
        if self.treeWidget.selectedItems() != []:
            self.lineEdit.setReadOnly(False)
            self.lineEdit_4.setReadOnly(False)
            self.lineEdit_5.setReadOnly(False)
            self.radioButton.setCheckable(True)
            self.radioButton_2.setCheckable(True)
        else:
            self.lineEdit.setReadOnly(True)
            self.lineEdit_4.setReadOnly(True)
            self.lineEdit_5.setReadOnly(True)
            self.radioButton.setCheckable(False)
            self.radioButton_2.setCheckable(False)

        return
    def updateTable(self):
        self.treeWidget.clear()
        person_groups = face_client.person_group.list(start=None, top=1000, return_recognition_model=False, custom_headers=None, raw=False)
        self.dic = {}
        self.totalPeople = 0;
        for PersonGroupObj in person_groups:
            self.dic[PersonGroupObj.name] = []
            people = face_client.person_group_person.list(PersonGroupObj.name, start=None, top=None, custom_headers=None, raw=False)
            for p in people:
                self.totalPeople = self.totalPeople + 1;
                data = p.user_data.split(',')
                self.dic[PersonGroupObj.name].append([p.name,data[0],data[1],data[2],data[3],data[4],data[5],p.person_id])
        keys= list(self.dic.keys())

       
        for i in range(0,len(self.dic[keys[0]])):
            row = QtWidgets.QTreeWidgetItem(self.treeWidget)
            row.setText(0,self.dic[keys[0]][i][0])
            row.setText(1,self.dic[keys[0]][i][4])
            row.setText(2,self.dic[keys[0]][i][2])
            row.setText(3,self.dic[keys[0]][i][3])
            row.setText(4,self.dic[keys[0]][i][1])
        return
    def modify(self):
        name = self.lineEdit.text()
        username = self.lineEdit_4.text()
        password = self.lineEdit_5.text()
        count = 0
        if(self.radioButton.isChecked()):
            count += 1
            status = "Admin"
        elif self.radioButton_2.isChecked():
            count += 1
            status = 'User'
        else:
            status = None
        selections = self.treeWidget.selectedItems()
        indexs = self.treeWidget.selectedIndexes()
        if selections != [] and indexs != []:
            person = selections[0].text(indexs[0].row())
            person_id = self.dic['test'][indexs[0].row()][-1]
            
            if name != '':    
                count += 1
                person = face_client.person_group_person.get('test',person_id)
                face_client.person_group_person.update(PERSON_GROUP_ID,person_id,name = name)
            if status != None:
                count += 1
                person = face_client.person_group_person.get('test',person_id)
                data = person.user_data.split(',')
                newData = data[0] + ',' + data[1] + ',' + data[2] + ',' + status + ',' + data[4] + ',' + data[5]
                face_client.person_group_person.update(PERSON_GROUP_ID,person_id,user_data = newData)
            if username != '':
                count += 1
                person = face_client.person_group_person.get('test',person_id)
                data = person.user_data.split(',')
                newData = data[0] + ',' + data[1] + ',' + data[2] + ',' + data[3] + ',' + username + ',' + data[5]
                face_client.person_group_person.update(PERSON_GROUP_ID,person_id,user_data = newData)
            if password != '':
                count += 1
                person = face_client.person_group_person.get('test',person_id)
                data = person.user_data.split(',')
                newData = data[0] + ',' + data[1] + ',' + data[2] + ',' + data[3] + ',' + data[4] + ',' + password
                face_client.person_group_person.update(PERSON_GROUP_ID,person_id,user_data = newData)

        self.updateTable()
        if (count != 0):
            self.statusbar.clearMessage()
            self.statusbar.setStyleSheet("color:green; font-size:14pt;")
            self.statusbar.showMessage("Successfully modified selected user.")

        else:
            self.statusbar.clearMessage()
            self.statusbar.setStyleSheet("color:red; font-size:14pt;")
            self.statusbar.showMessage("Please select a user from the user list to modify.")
        return
    def delete(self):
        people = []
        person_group_id = 'test'
        selections = self.treeWidget.selectedItems()
        indexs = self.treeWidget.selectedIndexes()
        
        person = (selections[0].text(indexs[0].row()))

        print("Total" + str(self.totalPeople))
        if self.totalPeople == 1:
            self.statusbar.clearMessage()
            self.statusbar.setStyleSheet("color:red; font-size:14pt;")
            self.statusbar.showMessage("At least one user need to be in the database!")

        else:
        
            person_id = self.dic[person_group_id][indexs[0].row()][-1]
            if person_id != self._person_id:
                face_client.person_group_person.delete(person_group_id, person_id, custom_headers=None, raw=False)
            else:
                self.statusbar.clearMessage()
                self.statusbar.setStyleSheet("color:red; font-size:14pt;")
                self.statusbar.showMessage("Don't delete yourself!")

        
        self.updateTable()
        return
    
        
    def loggout(self):
        person = face_client.person_group_person.get('test',self._person_id)
        data = person.user_data.split(',')

        newData = data[0] +','+ data[1] +  datetime.now().strftime(',%H:%M:%S,')  + data[-3] + ',' + data[-2] + ',' + data[-1]
        face_client.person_group_person.update(PERSON_GROUP_ID,self._person_id,user_data = newData)
        self.w.hide()
        print("go back to main page")
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui =  page1.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def goAddUser(self):
        self.w.hide()
        print("Go to add user page")
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui =  page4.Ui_MainWindow(self._name, self._person_id)
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        return 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow("Empty", "Person_ID")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


   