'''

Reference links:
#uickstart:
https://docs.microsoft.com/en-us/azure/cognitive-services/face/quickstarts/python-sdk
Face operations:
https://docs.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-face/azure.cognitiveservices.vision.face.operations?view=azure-python

'''


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
PERSON_GROUP_ID = 'test1'


''' 
Create the PersonGroup
'''
# Create empty Person Group. Person Group ID must be lower case, alphanumeric, and/or with '-', '_'.
print('Person group:', PERSON_GROUP_ID)

#(ONLY UNCOMMENT WHEN MAKING NEW PERSON GROUP)
#face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID,recognition_model='recognition_02', custom_headers=None, raw=False)
   

def captureImageFromVideo():
    
    video_capture = cv2.VideoCapture(0)
    
  
    i = 1 #used to increment the number of pictures taken
    
    while True:

        file_name = 'Brian'
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        frame = cv2.resize(frame,(960,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        cv2.imshow('Video', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('c'):
            
            file_name = '/Users/Brian/source/repos/Face group/Face group/' + file_name + str(i) + '.jpg'

            print ('Creating...' + file_name)
            cv2.imwrite(file_name, frame)
            
            IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)))

            
            image_array = glob.glob(os.path.join(IMAGES_FOLDER, file_name))
            image = open(image_array[0], 'r+b')

            # Detect faces
            faces = face_client.face.detect_with_stream(image, return_face_id=True, return_face_landmarks=True, return_face_attributes=['age', 'gender', 'headPose', 'smile', 'facialHair', 'glasses', 'emotion'], recognition_model='recognition_02', return_recognition_model=False, detection_model='detection_01', custom_headers=None, raw=False, callback=None)
    
            rectanle = faces[0].face_rectangle

            if ((rectanle.height > 200) and (rectanle.width> 200)):
                #only keep picture if race rectangle is bigger than 200 x 200 (azure reccomends)
                i+=1
            else:
                #remove image 
                image.close()
                os.remove(file_name)
            
        if i == 10:
            #takes 10 images
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    video_capture.release()
    cv2.destroyAllWindows()
    return

def getRectangle(faceDictionary):
    #function used to get rectangle dimensions from detected face object
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    bottom = left + rect.height
    right = top + rect.width
    return ((left, top), (bottom, right))

def getText(faceDictionary):
    #function used to get text location from detected face object

    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top - 10
    return (left,top)

def azureConnect():
    name = 'Brian'

    #creates new person in persongroup
    new_person = face_client.person_group_person.create(PERSON_GROUP_ID, name= 'Brian', user_data=None, recognition_model='recognition_02', custom_headers=None, raw=False)
    
    #assigns name of person in the persongroup

    new_person.name = name
    

    '''
    Detect faces and register to correct person
    '''
    # Find all jpeg images in working directory
    images = [file for file in glob.glob('*.jpg') if file.startswith(name)]
    print('Detected images: ',images)

    # Adds images to person in persongroup
    for image in images:
        b = open(image, 'r+b')
        face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, new_person.person_id, b)
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
            break
        elif (training_status.status is TrainingStatusType.failed):
            sys.exit('Training the person group has failed.')
    

    return

def main():
    captureImageFromVideo()
    azureConnect()
    return
main()

