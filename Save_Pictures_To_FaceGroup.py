'''
Reference links:

    #quickstart:
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


''' 
Create the PersonGroup
'''
# Create empty Person Group. Person Group ID must be lower case, alphanumeric, and/or with '-', '_'.
#(ONLY UNCOMMENT WHEN MAKING NEW PERSON GROUP)
#face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID,recognition_model='recognition_02', custom_headers=None, raw=False)
 
#used to store name of person which is also used as file name

#used to store the file path for all saved images
global path
path = '/Users/Brian/source/repos/Face group/Face group/'

    
if input('New person group? (Y/N): ').lower() == 'y':
    
    print()
    #note that person group id needs to be lower case
    PERSON_GROUP_ID = input('Enter person group name: ').lower()
    print()

    face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID,recognition_model='recognition_02', custom_headers=None, raw=False)
else:
    print()
    person_groups = face_client.person_group.list(start=None, top=1000, return_recognition_model=False, custom_headers=None, raw=False)
    for i in range(0,len(person_groups)):
        print(str(i+1) + '. ',person_groups[i].name)

    print()
    index = input('Enter the number for the corresponding person group you want to add to: ')
    PERSON_GROUP_ID = person_groups[int(index)-1].name
    print()
global Name
Name = input("Enter your name: ")
print()    



def main():
    '''
    The following code caputres a video using opencv, creates a new person in a person group, and adds the images to that person
    '''
    video_capture = cv2.VideoCapture(0)
    i = 1 #used to increment the number of pictures taken
    while True:

        # Capture frame-by-frame
        ret, frame = video_capture.read()
        #frame = cv2.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        cv2.imshow('Video', frame)
        
        
        file_name = path + Name + str(i) + '.jpg'

        print ('Creating...' + file_name)
        cv2.imwrite(file_name, frame)
            
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

                    i+=1
                else:
                    #remove image 
                    image.close()
                    os.remove(file_name)
            else:
                #remove image 
                image.close()
                os.remove(file_name)
            
            if i == 5:
                #takes 50 images
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                video_capture.release()
                cv2.destroyAllWindows()
                sys.exit()
    video_capture.release()
    cv2.destroyAllWindows()
    
    new_person = face_client.person_group_person.create(PERSON_GROUP_ID, name= Name, user_data=None, recognition_model='recognition_02', custom_headers=None, raw=False)
    new_person.name = Name

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
            break
        elif (training_status.status is TrainingStatusType.failed):
            sys.exit('Training the person group has failed.')
    

    return
main()
