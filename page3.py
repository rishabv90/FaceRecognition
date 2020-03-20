# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\risha\OneDrive\Desktop\faceRecGui\guiTest\guitTest1\page3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


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
path = "/Users/Julia/Documents/HWs/SeniorDesign/guitTest1/"

import page1, page4, page5

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

        #self.window = root
  
    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():

            self.vid.release()
            return
            
    def frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        else:
            return (ret, None)
    def get_frame(self):
        person_id = None
        accountType = 'User'
        flag = False
        if self.vid.isOpened():
            fps = self.vid.get(cv2.CAP_PROP_FPS)

            ret, frame = self.vid.read()
            results = []
            if ret:
                cv2.imwrite(path + "frame" + ".jpg",frame)
                # Return a boolean success flag and the current frame converted to BGR
                IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)))
                group_photo ='frame.jpg'


                # Get test image
                test_image_array = glob.glob(os.path.join(IMAGES_FOLDER, group_photo))
                print(IMAGES_FOLDER,path)
                image = open(test_image_array[0], 'r+b')

                # Detect faces
                face_ids = []
                faces = face_client.face.detect_with_stream(image, return_face_id=True, return_face_landmarks=True, return_face_attributes=['age', 'gender', 'headPose', 'smile', 'facialHair', 'glasses', 'emotion'], recognition_model='recognition_02', return_recognition_model=False, detection_model='detection_01', custom_headers=None, raw=False, callback=None)

                for face in faces:
                    #add face ids to face_ids list for .indentify() method
                    face_ids.append(face.face_id)

                # Identify faces
                # Check to make sure face was detected
                if face_ids != []:
                    results = face_client.face.identify(face_ids, PERSON_GROUP_ID)
                
                names = [] #stores names of person from .indentify ()
                confidence =[] #stores confidence of person from .indentify()
                    

                for person in results:
                    if person.candidates != []:
                 
                        try:
                            temp = face_client.person_group_person.get(PERSON_GROUP_ID, person.candidates[0].person_id, custom_headers=None, raw=False)
                        
                        except:
                            break

                        names.append(temp.name)
                        confidence.append(person.candidates[0].confidence)
                    else:
                    
                        results.remove(person)
                   
        
                faces = faces[:len(results)] #trim faces to match length of results
                count = 0 #used as incrementor for name, confidence lists
                for face in faces:
            
            

                    #draws string on image
                    font = cv2.FONT_HERSHEY_PLAIN
                    face_attributes = face.face_attributes
                    if confidence != []:
                        conf = int(confidence[count] * 100)
                        if conf >= 90:
                            color = (0,150,0)
                            flag = True

                            data = temp.user_data.split(',')
                            person_id = temp.person_id
                            newData = datetime.now().strftime('%m/%d/%Y,%H:%M:%S,') + '--------,'  + data[-3] + ',' + data[-2] + ',' + data[-1]
                            print(data)
       
                            accountType = data[-3]
                            print(accountType)
                            if (accountType == 'Admin'):
                                MainWindow.close()
                                self.window = QtWidgets.QMainWindow()
                                self.ui = page5.Ui_MainWindow5()
                                self.ui.setupUi(self.window)
                                self.window.show()

                            else:
                                MainWindow.close()
                                self.window = QtWidgets.QMainWindow()
                                self.ui = page4.Ui_MainWindow4()
                                self.ui.setupUi(self.window)
                                self.window.show()
               
                      
                            face_client.person_group_person.update(PERSON_GROUP_ID,temp.person_id,user_data = newData)
                        else:
                            color = (0,0,150)

                        text =  names[count] + ' Confidence: '+ str(conf) + '% ' + str(face_attributes.age) + ' '  + face_attributes.glasses
                        rect = face.face_rectangle
                        left = rect.left
                        top = rect.top
                        bottom = left + rect.height
                        right = top + rect.width

                        tleft = rect.left - (int(rect.width/2))
                        ttop = rect.top - 20
                        dim = (tleft,ttop)

                        v1 = (left, top)
                        v2 = (bottom, right)
                        cv2.rectangle(frame,v1,v2,color, 1)
                        cv2.putText(frame,text,dim,font, 1.5,color, 1, cv2.LINE_AA)
                        cv2.imwrite(path + "frame" + ".jpg",frame)

                        count += 1 
                        image.close()

                return (test_image_array[0],accountType,person_id,flag)
            else:
                

                return (None,accountType,person_id,flag)
        else:
            return (None,accountType,person_id,flag)


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2000, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(780, 10, 261, 41))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(780, 50, 231, 171))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(704, 800, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.vid = MyVideoCapture(video_source = 0)




        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(1500, 280, 121, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1500, 340, 121, 31))
        self.lineEdit.setObjectName("lineEdit")
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

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        #button links
        self.pushButton_2.clicked.connect(self.goToPage1)

        self.flag = False
        self.timer = QtCore.QTimer(self.centralwidget)
        self.timer.setSingleShot(False)
        self.timer.setInterval(100) # in milliseconds, so 5000 = 5 seconds
        self.timer.timeout.connect(self.update)
        self.timer.start()
        
      

    def update(self):
        if self.flag == False:
            imagePath,self._accountType,self._person_id,self.flag = self.vid.get_frame()
            print(self.flag)
            if imagePath != None:
                self.image = QtGui.QPixmap(imagePath)
            
                self.label2.setPixmap(self.image)
                self.label2.setGeometry(QtCore.QRect(680, 260, 641, 481))
        return
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Facial recognition</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"Webp.net-resizeimage.jpg\"/></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Go back to main Page"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Status:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p></body></html>"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))

    def goToPage1(self):
        #MainWindow.close()
        print("go back to main page")
        self.window = QtWidgets.QMainWindow()
        self.ui =  page1.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
