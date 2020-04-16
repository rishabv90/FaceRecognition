# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\risha\OneDrive\Desktop\faceRecGui\guiTest\guitTest1\page6.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
# Add user's page (for admin use only)

#from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2 import QtCore, QtGui, QtWidgets
import datetime
from threading import Timer
import asyncio, io, glob, os, sys, time, uuid, requests, cv2
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType
import page2, page3, page5

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

class MyVideoCapture: 
    def __init__(self, video_source=0):
        #open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.start_time = time.time()
  

    def __del__(self):
        if self.vid.isOpened():

            self.vid.release()
            return

    def frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            return (ret, frame)
        else:
            return (ret, None)

class Ui_MainWindow(object):
    def __init__(self, currentAdmin, personID):
        self.adminName = currentAdmin
        self.newName = ""
        self.newUserName = ""
        self.newPassword = ""
        self.status = ""
        self._i = 0
        self._j = 0
        self._adminPersonID = personID

    def setupUi(self, MainWindow):
        self.w = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1138, 899)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vlabel = QtWidgets.QLabel(self.centralwidget)
        self.vlabel.setGeometry(QtCore.QRect(470, 180, 651, 581))
        self.vlabel.setObjectName("graphicsView")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 720, 151, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(240, 370, 91, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(360, 370, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        #Name
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 210, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        #Password
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 270, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        #username
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 320, 211, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 410, 401, 161))
        self.label_10.setObjectName("label_10")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 560, 211, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 720, 151, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 561, 61))
        self.label_2.setObjectName("label_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1000, 10, 111, 51))
        self.label_11.setStyleSheet("image: url(samPicture.jpg);")
        self.label_11.setText("")
        self.label_11.setTextFormat(QtCore.Qt.PlainText)
        self.label_11.setPixmap(QtGui.QPixmap("samPicture.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 190, 221, 61))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 250, 221, 61))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 300, 221, 61))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 350, 221, 61))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(30, 610, 251, 61))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(320, 610, 651, 61))
        self.label_17.setObjectName("label_17")
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

        self.timer = QtCore.QTimer(self.centralwidget)
        self.timer.setSingleShot(False)
        self.timer.setInterval(1)
        self.timer.start()
        self.timer.timeout.connect(self.showVideo)

        self.timer2 = QtCore.QTimer(self.centralwidget)
        self.timer2.setSingleShot(False)
        self.timer2.setInterval(1)
        self.timer2.start()


        self._vid = MyVideoCapture(video_source = 0)

        #collecting faces 
        self.pushButton_4.clicked.connect(self.click)
        #cancel button
        self.pushButton_5.clicked.connect(self.goToAdmin)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))
        self.radioButton.setText(_translate("MainWindow", "Administrative"))
        self.radioButton_2.setText(_translate("MainWindow", "Regular User"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Instructions:- </span></p><p><span style=\" font-size:12pt;\">- Please get ready to get 25 clear pictures clicked. </span></p><p><span style=\" font-size:12pt;\">- Please present a clear view to the camera.</span></p><p><span style=\" font-size:12pt;\">- Please provide variation by Left/Right head movement.</span></p><p><br/></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Begin face Recognition Collection"))
        self.pushButton_5.setText(_translate("MainWindow", "Cancel"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Create New User by Admin - " + self.adminName +"</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter your name :</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter your password :</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter your username :</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter your Status :</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Face recognition collection status :</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">0/25</span></p></body></html>"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))

    def changeRed(self):
        _translate = QtCore.QCoreApplication.translate
        if self.radioButton.isChecked() == False and self.radioButton_2.isChecked() == False:
            self.label_15.setStyleSheet("font-size:12pt; color:red;")
        if self.nameField == False:
            self.label_12.setStyleSheet("font-size:12pt; color:red;")
            self.lineEdit.setStyleSheet("border: 2px solid red;")
        if self.pwdField == False:
            self.label_13.setStyleSheet("font-size:12pt; color:red;")
            self.lineEdit_2.setStyleSheet("border: 2px solid red;")
        if self.userField == False:
            self.label_14.setStyleSheet("font-size:12pt; color:red;")
            self.lineEdit_3.setStyleSheet("border: 2px solid red;")
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:red;\">Please enter all the required fields first</span></p></body></html>"))
      
        t = Timer(2.0, self.changeBlack)
        t.start()

    def changeBlack(self):
        self.nameField = True
        self.pwdField = True
        self.userField = True
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.setStyleSheet("border: 1px solid black;")
        self.lineEdit_2.setStyleSheet("border: 1px solid black;")
        self.lineEdit_3.setStyleSheet("border: 1px solid black;")
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:black;\">Enter your name :</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:black;\">Enter your password :</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:black;\">Enter your username :</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:black;\">Enter your Status :</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:black;\">0/25</span></p></body></html>"))

    def showVideo(self):
        file_name = path + "temp" + '.jpg'
        ret, frame = self._vid.frame()
        cv2.imwrite(file_name, frame)
        self.qtImage = QtGui.QPixmap(file_name)
        self.vlabel.setPixmap(self.qtImage)
        self.vlabel.setGeometry(QtCore.QRect(470, 190, 681, 341))
        return

    def click(self):
        self.nameField = True
        self.pwdField = True
        self.userField = True
     
        if self.lineEdit.text() == "":
            self.nameField = False
        if self.lineEdit_2.text() == "":
            self.pwdField = False
        if self.lineEdit_3.text() == "":
            self.userField = False

        if self.nameField == True and self.pwdField == True and self.userField == True and (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.timer2.timeout.connect(self.addPic)
            self.timer.stop()
        else:
            self.changeRed()
        

    def addPic(self):

        Name = self.lineEdit.text()

        if self._i < 25:
            ret, frame = self._vid.frame()
           
            file_name = path + Name + str(self._i) + '.jpg'

            self.label_17.clear()
            html = "<html><head/><body><p><span style=\" font-size:12pt;\"><b>" + str(self._i + 1) + "</b>/25</span><span style=\"font-size:10pt; color:red\"> (Move closer if the number is not increasing)</span></p></body></html>"
            self.label_17.setText(html)
            cv2.imwrite(file_name, frame)
            self.qtImage = QtGui.QPixmap(file_name)
            self.vlabel.setPixmap(self.qtImage)
            self.vlabel.setGeometry(QtCore.QRect(470, 190, 681, 341))

            if self._j % 25 == 0:
                image_array = glob.glob(os.path.join(path, file_name))
                if image_array:
                    image = open(image_array[0], 'r+b')

                    # Detect faces
                    faces = face_client.face.detect_with_stream(image, return_face_id=True, return_face_landmarks=True, return_face_attributes=['age', 'gender', 'headPose', 'smile', 'facialHair', 'glasses', 'emotion'], recognition_model='recognition_02', return_recognition_model=False, detection_model='detection_01', custom_headers=None, raw=False, callback=None)
                    print(len(faces))
                    print(faces)
                    if faces != [] and len(faces) < 2:
                        rectanle = faces[0].face_rectangle
                        if rectanle.height > 200 and rectanle.width> 200:
                            #only keep picture if race rectangle is bigger than 200 x 200 (azure reccomends)

                            self._i+=1

                        else:
                          
                            #remove image 
                            image.close()
                            os.remove(file_name)
                    else:
                        #remove image 
                        image.close()
                        os.remove(file_name)
            
            

        if self._i == 25:
            self.label_17.clear()
            self.label_17.setGeometry(QtCore.QRect(320, 610, 451, 91))
            doneText = "<html><head/><body><p><span style=\" font-size:12pt; color:green\"><b> DONE</b><br />Please click <b><u>Save</u></b> to continue.<br />If you want to cancel the registration, just click <b><u>Cancel</u></b>.</span></p></body></html>"
            self.label_17.setText(doneText)
            try:
              del self._vid
            except:
              return 0
            #save button
            self.pushButton_3.clicked.connect(self.addPicClicked)
            

        #to loop through the process of taking pictures
        self._j+=1
        return

    def addPicClicked(self):
        
        if(self.radioButton.isChecked()):
            self.status = "Admin"
           
        else:
            self.status = "User"

        self.newUserName = self.lineEdit_3.text()
        self.newName = self.lineEdit.text()
        self.newPassword = self.lineEdit_2.text()
        addName = self.newName
        addUserName = self.newUserName
        addPwd = self.newPassword
        addStatus = self.status

        Name = addName
        data = ''
        t = '--------,' + '--------,'
        t2 = '--------,'
        data = t + t2 + addStatus +',' +addUserName+ ','+addPwd 
        self.statusbar.clearMessage()
        self.statusbar.setStyleSheet("color: blue; font-size: 15pt;")
        self.statusbar.showMessage(data)
       
  
        new_person = face_client.person_group_person.create(PERSON_GROUP_ID, name= Name, user_data=data, custom_headers=None, raw=False)
        new_person.name = Name
        new_person.user_data = data
        '''
        Detect faces and register to correct person
        '''
        # Find all jpeg images in working directory
    

        # Adds images to person in persongroup
    
    
        for i in range(1,25):
            file_name = path + Name + str(i) + '.jpg'
            image_array = glob.glob(os.path.join(path, file_name))
            print('Adding: ',image_array[0])
            image = open(image_array[0], 'r+b')
            face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, new_person.person_id, image)
            image.close()
   
        for i in range(1,25):
            file_name = path + Name + str(i) + '.jpg'
            image_array = glob.glob(os.path.join(path, file_name))

            try:
                print('Removing: ',image_array[0])
                os.remove(file_name)
            except:
                print('Didnt remove: ',file_name)

    
    

        ''' 
        Train PersonGroup
        '''
        print()
        print('Training the person group...')
        # Train the person group
        face_client.person_group.train(PERSON_GROUP_ID)

        while (True):
            training_status = face_client.person_group.get_training_status(PERSON_GROUP_ID)
            print("Training status: {}.".format(training_status.status))
            print()
            if (training_status.status is TrainingStatusType.succeeded):
                self.goToAdmin()
                #if (self.status == "Admin"):
                #    self.goToAdmin()

                #else:
                #    self.goToNormal()
          
                return
                
            elif (training_status.status is TrainingStatusType.failed):
                sys.exit('Training the person group has failed.')
        return
        
  
    def goToAdmin(self): #if the submit button is clicked and is registered as an 'admin', then go to the admin page
        self.w.hide()
        print("Go to add user page")
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui =  page5.Ui_MainWindow(self.adminName, self._adminPersonID)
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow("Empty", "Admin PersonID")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
