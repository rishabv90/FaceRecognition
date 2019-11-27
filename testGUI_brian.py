from tkinter import *
import PIL.Image, PIL.ImageTk


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
ENDPOINT = "https://testface19025.cognitiveservices.azure.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=true&returnFaceAttributes=[age,gender,glasses]&recognitionModel=recognition_02&returnRecognitionModel=false&detectionModel=detection_01"

global face_client
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

 
# Used in the Person Group Operations,  Snapshot Operations, and Delete Person Group examples.
# You can call list_person_groups to print a list of preexisting PersonGroups.
# SOURCE_PERSON_GROUP_ID should be all lowercase and alphanumeric. For example, 'mygroupname' (dashes are OK).
global PERSON_GROUP_ID
PERSON_GROUP_ID = 'test'

global path
path = '/Users/Brian/source/repos/Face group/Face group/'

class MyVideoCapture: 
    def __init__(self, video_source=0):
        #open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
  
    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
        self.window.mainloop()

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                cv2.imwrite(path + "frame" + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                # Return a boolean success flag and the current frame converted to BGR
                IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)))
                group_photo ='frame.jpg'
                # Get test image
                test_image_array = glob.glob(os.path.join(IMAGES_FOLDER, group_photo))
                image = open(test_image_array[0], 'r+b')
                print(IMAGES_FOLDER)
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
                if not results:
                    print('No person identified in the person group'.format(os.path.basename(image.name)))
                for person in results:
                    if person.candidates != []:
                   
                    
                        #.get() used to return person object in persongroup
                        temp = face_client.person_group_person.get(PERSON_GROUP_ID, person.candidates[0].person_id, custom_headers=None, raw=False)

                        names.append(temp.name)
                        confidence.append(person.candidates[0].confidence)
                        print('Person: {}    Confidence: {}.'.format(temp.name, person.candidates[0].confidence)) # Get topmost confidence score
                    else:
                    
                        results.remove(person)
                   
        
                faces = faces[:len(results)] #trim faces to match length of results
                print(confidence)
                count = 0 #used as incrementor for name, confidence lists
                for face in faces:
            
            
            
                    #cv2.rectangle(frame, (x, y), (x+w, y+h), (150, 140, 150), 2)

                    #draws string on image
                    font = cv2.FONT_HERSHEY_PLAIN
                    #cv2.putText(frame,'OpenCV Tuts!',(x,y), font, 1,(200,255,155), 1, cv2.LINE_AA)
                    face_attributes = face.face_attributes
                    if confidence != []:
                        conf = int(confidence[count] * 100)
                        if conf >= 95:
                            color = (0,150,0)
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
                        count += 1 
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)
class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        #open video source

        self.vid = MyVideoCapture(video_source)
        #create a canvas that can fit the above video source size
        self.canvas = Canvas(self.window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()
            

        #snapshot button
        self.btn_snapshot= Button(window, text="Add New User", width=50, command=self.snapshot, bg="black", fg="white")
        self.btn_snapshot.pack(anchor=CENTER, expand=True)
        self.snapshot()
        self.delay = 5
        self.update()
        
        self.window.mainloop()
    
    def update(self):
        #Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
        self.window.after(self.delay, self.update)

    def snapshot(self):
         #Get a frame from the video source
         ret, frame = self.vid.get_frame()
         print("capture")
         if ret:
            cv2.imwrite(path + "frame" + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            
        
# Create a window and pass it to the Application object
root = Tk()
App(root, "Tkinter and OpenCV")
