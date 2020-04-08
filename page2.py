
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\risha\OneDrive\Desktop\faceRecGui\guiTest\guitTest1\page2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets
import page3, page1, page5
import time
from threading import Timer
import datetime
#from page2 import Ui_MainWindow2
#x.getDatabase
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType
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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1138, 902)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(520, 320, 231, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setGeometry(QtCore.QRect(520, 370, 231, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 500, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(940, 790, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 351, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 310, 221, 61))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1000, 10, 111, 51))
        self.label_5.setStyleSheet("image: url(:/test2/samPicture.jpg);")
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setPixmap(QtGui.QPixmap(":/test2/samPicture.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(360, 360, 221, 61))
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 420, 500, 50))
        self.label.setObjectName("label")
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

        self.pushButton.clicked.connect(self.submitClicked)  #submit typed in credentials
        self.pushButton_2.clicked.connect(self.goToMainPage) #back to main page

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton_2.setText(_translate("MainWindow", "Face Recognition"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Manual Login</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Username :</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Password :</span></p></body></html>"))
        #self.label.setText(_translate("MainWindow", "ENTER MESSAGE HERE XXXXXXXXXX"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))

    def goToMainPage(self):#back to main page button
        MainWindow.close()
        print("go back to main page")
        self.window = QtWidgets.QMainWindow()
        self.ui =  page1.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def submitClicked(self):#if submit button pressed
        print('userName = '+self.lineEdit.text())   #user input username
        print('password = '+self.lineEdit_2.text()) #user input password
        userName = self.lineEdit.text()
        password = self.lineEdit_2.text()

     
        person_groups = face_client.person_group.list(start=None, top=1000, return_recognition_model=False, custom_headers=None, raw=False)
        dic = {}
        for PersonGroupObj in person_groups:
            dic[PersonGroupObj.name] = []
            people = face_client.person_group_person.list(PersonGroupObj.name, start=None, top=None, custom_headers=None, raw=False)
            for p in people:
                data = p.user_data.split(',')
       
               #0:date, 1:login time, 2: logout time, 3: status, 4: user name, 5: pwd
                dic[PersonGroupObj.name].append([data[3], data[4],data[5]])

        keys = list(dic.keys())  
        done = 0
        count = 0;
        for key in keys:
            print(dic[key])
            for human in dic[key]:
                count = count + 1 
                if (userName == human[1]):
                    if (password == human[2]):
                        #password matches for login                   
                        if (human[0] == "Admin"):
                           # print('logged in as an Admin')
                            
                           # MainWindow.close()
                            #MainWindow.hide()
                            self.window = QtWidgets.QMainWindow()
                            #**********************************TODO: Change human[1] to actual user's 'Name' instead of 'username'**********************************
                            self.ui =  page5.Ui_MainWindow(human[1])
                            self.ui.setupUi(self.window)
                            self.window.show()
                 

                        else:
                            print('logged in as a normal user')
                            #MainWindow.close()
                            #MainWindow.hide()
                            self.window = QtWidgets.QMainWindow()
                            #**********************************TODO: Change human[1] to actual user's 'Name' instead of 'username'***********************************
                            self.ui =  page3.Ui_MainWindow(human[1])
                            self.ui.setupUi(self.window)
                            self.window.show()
                        
                        r = Timer(20.0, MainWindow.hide())
                        r.start()

                    else: 
                        self.changeToRed()
                        print("password doesn't match the username")

                else:
                    done = done + 1

        if(count == done):
            self.changeToRed()
            print("no username found in the database")
            #msg = QtWidgets.QMessageBox()
            #msg.setWindowTitle("Error")
            #msg.setText("Username does not exist or wrong password")
            #x = msg.exec_() 

    def changeToRed(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:red;\">Username :</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:red;\">Password :</span></p></body></html>"))
        self.lineEdit.setStyleSheet("border: 2px solid red;")
        self.lineEdit_2.setStyleSheet("border: 2px solid red;")
        self.label.setStyleSheet("font-size:12pt; color:red;")
        self.label.setText("Check your username/password,\nthe user might not exist or the password doesn't match the username.")
        #self.statusbar.showMessage("Check your username/password, the user might not exist or the password doesn't match the username")
        #self.statusbar.setStyleSheet("font-size: 14pt; color: red")
        t = Timer(2.0, self.changeBlack)
        t.start()

    def changeBlack(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:800; color:black;\">Username :</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:800; color:black;\">Password :</span></p></body></html>"))
        self.lineEdit.setStyleSheet(_translate("MainWindow", "border: 1px solid black;"))
        self.lineEdit_2.setStyleSheet("border: 1px solid black;")
        self.label.setText("")
        #self.statusbar.clearMessage()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
