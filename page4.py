# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\risha\OneDrive\Desktop\faceRecGui\guiTest\guitTest1\page6.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
# Add user's page (for admin use only)

from PySide2 import QtCore, QtGui, QtWidgets
from datetime import *
import asyncio, io, glob, os, sys, time, uuid, requests, cv2
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
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
#path = "/Users/Julia/Documents/HWs/SeniorDesign/guitTest1/"
path = "/Users/Julia/source/repos/updateGUI/"
import page2, page3, page1

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
    def __init__(self):
        self.newName = ""
        self.newUserName = ""
        self.newPassword = ""
        self.status = ""
        self._i = 0;

    def setupUi(self, MainWindow):
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
        #password = lineEdit
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 270, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        #username = lineEdit_2
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 320, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        #Name = lineEdit_3
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 210, 211, 31))
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
        self.label_17.setGeometry(QtCore.QRect(320, 610, 251, 61))
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
        self.timer2.setInterval(100)
        self.timer2.start()


        self._vid = MyVideoCapture(video_source = 0)

        #********TODO********** For the button clicks
        #cancel button
        self.pushButton_5.clicked.connect(self.goToPage1)
        #save button
        self.pushButton_3.clicked.connect(self.addPic)
        #collecting faces button
        self.pushButton_4.clicked.connect(self.addPic)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))
        self.radioButton.setText(_translate("MainWindow", "Administrative"))
        self.radioButton_2.setText(_translate("MainWindow", "Regular User"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Instructions:- </span></p><p><span style=\" font-size:12pt;\">- Please get ready to get 25 clear pictures clcicked. </span></p><p><span style=\" font-size:12pt;\">- Please present a clear view to the camera.</span></p><p><span style=\" font-size:12pt;\">- Please provide variation by Left/Right head movement.</span></p><p><br/></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Begin face Recognition Collection"))
        self.pushButton_5.setText(_translate("MainWindow", "Cancel"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Create New User by Admin</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter your name :</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter your password :</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter your username :</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter your Status :</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Face recognition collection status :</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">XX/25</span></p></body></html>"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))

    def showVideo(self):
        file_name = path + "temp" + '.jpg'
        ret, frame = self._vid.frame()
        cv2.imwrite(file_name, frame)
        self.qtImage = QtGui.QPixmap(file_name)
        self.vlabel.setPixmap(self.qtImage)
        self.vlabel.setGeometry(QtCore.QRect(470, 190, 381, 341))
        return

    def addPic(self):
        self.timer.stop()

        Name = self.lineEdit_3.text()
        if self._i < 5:
            ret, frame = self._vid.frame()
           # self._photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            
            
            file_name = path + Name + str(self._i) + '.jpg'

            print ('Creating...' + file_name)
            cv2.imwrite(file_name, frame)
            self.qtImage = QtGui.QPixmap(file_name)
            self.vlabel.setPixmap(self.qtImage)
            self.vlabel.setGeometry(QtCore.QRect(470, 190, 381, 341))

            IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)))
            
            image_array = glob.glob(os.path.join(IMAGES_FOLDER, file_name))
            if image_array:
                image = open(image_array[0], 'r+b')

                # Detect faces
                faces = face_client.face.detect_with_stream(image, return_face_id=True, return_face_landmarks=True, return_face_attributes=['age', 'gender', 'headPose', 'smile', 'facialHair', 'glasses', 'emotion'], recognition_model='recognition_02', return_recognition_model=False, detection_model='detection_01', custom_headers=None, raw=False, callback=None)
                if faces != []:
                    rectanle = faces[0].face_rectangle

                    if ((rectanle.height > 200) and (rectanle.width> 200)):
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
            
            

        if self._i == 5:
            try:
              del self._vid
            except:
              return 0

            self.addPicClicked()
        #to loop through the process of taking pictures
       
        self.timer2.timeout.connect(self.addPic)
        return

    def addPicClicked(self):
        
        if(self.radioButton.isChecked()):
            self.status = "Admin"
           
        else:
            self.status = "User"

        self.newUserName = self.lineEdit_2.text()
        self.newName = self.lineEdit_3.text()
        self.newPassword = self.lineEdit.text()
        addName = self.newName
        addUserName = self.newUserName
        addPwd = self.newPassword
        addStatus = self.status

        Name = addName
        data = ''
        t = datetime.now().strftime('%m/%d/%Y,%H:%M:%S,')
        t2 = datetime.now().strftime('%H:%M:%S,')
        data = t + t2 + addStatus +',' +addUserName+ ','+addPwd 
        print(data)
        self.statusbar.clearMessage()
        self.statusbar.setStyleSheet("color: blue; font-size: 15pt;")
        self.statusbar.showMessage(data)
       
  
        new_person = face_client.person_group_person.create(PERSON_GROUP_ID, name= Name, user_data=data, custom_headers=None, raw=False)
        new_person.name = Name
        new_person.user_data = data
        print(new_person.user_data)
        '''
        Detect faces and register to correct person
        '''
        # Find all jpeg images in working directory
    

        # Adds images to person in persongroup
        IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    
    
        for i in range(1,5):
            file_name = path + Name + str(i) + '.jpg'
            image_array = glob.glob(os.path.join(IMAGES_FOLDER, file_name))
            print('Adding: ',image_array[0])
            image = open(image_array[0], 'r+b')
            face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, new_person.person_id, image)
            image.close()
        print()
   
        for i in range(1,5):
            file_name = path + Name + str(i) + '.jpg'
            image_array = glob.glob(os.path.join(IMAGES_FOLDER, file_name))

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
                if (self.status == "Admin"):
                    self.goToAdmin()

                else:
                    self.goToNormal()
          
                return
                
            elif (training_status.status is TrainingStatusType.failed):
                sys.exit('Training the person group has failed.')
        return
        

    #**********TODO:Not yet implemented**********
    def goToPage1(self):#if the cancel button is clicked, go back to the main facial recognition page
        MainWindow.close()
        print("logout")
        self.window = QtWidgets.QMainWindow()
        self.ui = page1.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()   
  
    def goToAdmin(self): #if the submit button is clicked and is registered as an 'admin', then go to the admin page
        MainWindow.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = page5.Ui_MainWindow(self.newName)
        self.ui.setupUi(self.window)
        self.window.show()

    def goToNormal(self): #if the submit button is clicked and is registered as a 'normal', then go to the normal user page
        MainWindow.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = page3.Ui_MainWindow(self.newName)
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
