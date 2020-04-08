# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\risha\OneDrive\Desktop\faceRecGui\guiTest\guitTest1\page3_update.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
# Facial Recognition Page (START UP PAGE)

from PySide2 import QtCore, QtGui, QtWidgets
from datetime import *
import asyncio, io, glob, os, sys, time, uuid, requests, cv2
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType
import azure.cognitiveservices.speech as speechsdk
import time
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

speech_key, service_region = '164834d14ca54cb5a17189f508abf0ff', "westus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
 
# Used in the Person Group Operations,  Snapshot Operations, and Delete Person Group examples.
# You can call list_person_groups to print a list of preexisting PersonGroups.
# SOURCE_PERSON_GROUP_ID should be all lowercase and alphanumeric. For example, 'mygroupname' (dashes are OK).
global PERSON_GROUP_ID
PERSON_GROUP_ID = 'test'

global path
#path = "/Users/Julia/Documents/HWs/SeniorDesign/guitTest1/"
path = "/Users/Julia/source/repos/updateGUI/"
import page2, page3, page5

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
                finalPerson = [] #stores the name of the final person who was identified    

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
                            finalPerson = data[-2]
       
                            accountType = data[-3]
                            
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
                        finalPerson = names[count]
                        count += 1 
                        image.close()

                return (test_image_array[0],accountType,person_id,flag,finalPerson)
            else:
                

                return (None,accountType,person_id,flag,finalPerson)
        else:
            return (None,accountType,person_id,flag,finalPerson)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1137, 922)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(860, 800, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 780, 221, 71))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 401, 61))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1000, 10, 111, 51))
        self.label_5.setStyleSheet("image: url(samPicture.jpg);")
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setPixmap(QtGui.QPixmap("samPicture.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 780, 601, 71))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1137, 21))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuExit.menuAction())

        self.pushButton.clicked.connect(self.goToManual)
        self.vid = MyVideoCapture(video_source = 0)
        #for live video feed
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 120, 871, 641))
        self.label_7.setObjectName("label_7")

        self.flag = False
        self.timer = QtCore.QTimer(self.centralwidget)
        self.timer.setSingleShot(False)
        self.timer.setInterval(100) # in milliseconds, so 5000 = 5 seconds

        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
        check = True

        while check == True:
            now = datetime.now().time()
            if now.hour<17  and now.hour>=7:
                time.sleep(3)
                print("Please Instruct System to Begin Facial Recognition by saying 'Wake Up'")
                result = speech_recognizer.recognize_once()

            # Checks result.
                if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                    if  result.text == 'Wake up.':
                        print("Thank you for your input, the system will now begin facial recognition")
                        self.timer.timeout.connect(self.update)
                        check = False
        
                    else:
                        print("Recognized: {}".format(result.text))
                        print("This Statement is not a valid input for our system please try again")
        
                elif result.reason == speechsdk.ResultReason.NoMatch:
                    print("No speech could be recognized: {}".format(result.no_match_details))
                elif result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = result.cancellation_details
                    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
                    if cancellation_details.reason == speechsdk.CancellationReason.Error:
                        print("Error details: {}".format(cancellation_details.error_details))

        #self.timer.timeout.connect(self.update)
        self.timer.start()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def goToManual(self): #direct to manual login page
        #MainWindow.close()
        MainWindow.hide()
        print("Go to manual login page")
        self.window = QtWidgets.QMainWindow()
        self.ui = page2.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        return 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Manual Login"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Status :</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Facial Recognition Login</span></p></body></html>"))
        #self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Insert Status here XXXXXXXXXXXXXX</span></p></body></html>"))
        self.label_6.setStyleSheet(_translate("MainWindow", "font-size:11pt; color:blue;"))
        self.label_6.setText(_translate("MainWindow", "Please present your face, the live video feed will start soon"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.statusbar.setStyleSheet("font-size:15pt; color: blue;")
        self.statusbar.showMessage("Please present your face in front of the camera without accessories covering your face to allow the system to identify your face")
    
    def update(self):
            if self.flag == False:
                imagePath,self._accountType,self._person_id,self.flag, self._identifiedPerson = self.vid.get_frame()
                print(self.flag,self._accountType)
                            
                if imagePath != None:
                    self.label_6.setStyleSheet("font-size:11pt; color: red;")
                    self.label_6.setText("Please show your face clearly to the camera or check the lighting.")
                    self.image = QtGui.QPixmap(imagePath)
                    self.label_7.setPixmap(self.image)
            else:
                self.timer.stop()
                self.showStatus(self._identifiedPerson, self._accountType)
                self.label_6.setStyleSheet("font-size:11pt; color: green;")
                self.label_6.setText("Successfully loggin you in")
                time.sleep(3)
                #self.showLogin(self._identifiedPerson)
                
                del self.vid
                if (self._accountType == 'Admin'):
                    #MainWindow.close()
                    MainWindow.hide()
                    self.window = QtWidgets.QMainWindow()
                    self.ui = page5.Ui_MainWindow(self._identifiedPerson)
                    self.ui.setupUi(self.window)
                    self.window.show()
     
                else:
                    #MainWindow.close()
                    MainWindow.hide()
                    self.window = QtWidgets.QMainWindow()
                    self.ui = page3.Ui_MainWindow(self._identifiedPerson)
                    self.ui.setupUi(self.window)
                    self.window.show()
            return

    def showStatus(self, person, type): #TODO
        _translate = QtCore.QCoreApplication.translate
        self.label_6.setStyleSheet(_translate("MainWindow", "font-size:14pt; color:green"))
        self.label_6.setText(_translate("MainWindow", "Logging" + person + " in as " + type))
        
        #time.sleep(3)
  


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())