# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\risha\OneDrive\Desktop\faceRecGui\guiTest\guitTest1\page6.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from datetime import *
import asyncio, io, glob, os, sys, time, uuid, requests, cv2
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType

from PySide2 import QtCore, QtGui, QtWidgets
import page1
import page2

global KEY
KEY = '12f952f3b226421aa2019ab14740b123'
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
#Change
path = "/Users/Julia/Documents/HWs/SeniorDesign/guitTest1/"

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


class Ui_MainWindow6(object):
    def __init__(self):
        self.newName = ""
        self.newUserName = ""
        self.newPassword = ""
        self.status = ""
        self._i = 0;


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 652)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(190, 10, 391, 51))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 40, 231, 171))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(704, 562, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 210, 151, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 240, 151, 21))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 270, 151, 21))
        self.textEdit_4.setObjectName("textEdit_4")

        #self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        #self.graphicsView.setGeometry(QtCore.QRect(470, 190, 381, 341))
        #self.graphicsView.setObjectName("graphicsView")
        self.vlabel = QtWidgets.QLabel(self.centralwidget)



  
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 210, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 240, 171, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 270, 171, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 330, 151, 21))
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 460, 151, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 330, 171, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(20, 300, 151, 21))
        self.textEdit_6.setObjectName("textEdit_6")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(200, 300, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(280, 300, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 21))
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
        self.timer.setInterval(100)
        self.timer.start()

        self._vid = MyVideoCapture(video_source = 0)

        self.pushButton_3.clicked.connect(self.addPic)
        self.pushButton_2.clicked.connect(self.goToPage1)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Admin: Create New user</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"Webp.net-resizeimage.jpg\"/></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Logout"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Enter your name:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Enter your Username:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Enter your Password:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p></body></html>"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">face Rec Status:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Submit"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Enter your status:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p></body></html>"))
        self.radioButton.setText(_translate("MainWindow", "Admin"))
        self.radioButton_2.setText(_translate("MainWindow", "normal"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))

    def addPic(self):
        Name = self.lineEdit.text()
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

            self.submitClicked()
        #to loop through the process of taking pictures
       
        self.timer.timeout.connect(self.addPic)
        return

    def submitClicked(self):
        
        if(self.radioButton.isChecked()):
            self.status = "Admin"
           
        else:
            self.status = "User"
        print("new name = " + self.lineEdit.text())
        self.newName = self.lineEdit.text()
        self.newUserName = self.lineEdit_2.text()
        self.newPassword = self.lineEdit_3.text()
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
        #print(data)
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
                self.goToPage1()
                return
                
            elif (training_status.status is TrainingStatusType.failed):
                sys.exit('Training the person group has failed.')
        return
        

        
    def goToPage1(self):#logout button
        MainWindow.close()
        print("logout")
        self.window = QtWidgets.QMainWindow()
        self.ui = page1.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()   
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow6()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

