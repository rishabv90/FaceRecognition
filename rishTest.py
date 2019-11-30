
from libs import *
global FACE_SUBSCRIPTION_KEY
global ENDPOINT
global flag


#Keys and function calls.
FACE_SUBSCRIPTION_KEY = '12f952f3b226421aa2019ab14740b123'
ENDPOINT = "https://testface19025.cognitiveservices.azure.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=true&returnFaceAttributes=[age,gender,glasses]&recognitionModel=recognition_02&returnRecognitionModel=false&detectionModel=detection_01"
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(FACE_SUBSCRIPTION_KEY))


def captureImageFromVideo():
    
    video_capture = cv2.VideoCapture(0) #from webcam
    i = 0 #counter for number of images taken
    userName = input("Please enter your name : ") # take an input from user for GUI - account creation
    filePath = "/Users/risha/OneDrive/Desktop/visualStudio/" + userName  #change according to your directory
    flag = True
    
    

    ##%%%%%%Need to make new folders for each user and delete after creating person groups.

    while True:
   
        ret, frame = video_capture.read()
        frame = cv2.resize(frame,(960,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        cv2.imshow('Video', frame)                  

        if (cv2.waitKey(1) & 0xFF == ord('p')): ##JULIA WORK - need to take picture on button press from GUI rather than p right now
            print("Picture taken for user: " + userName)
            filePathExtension = str(i) + ".jpg";
            print ('Image saved at ' + filePath+filePathExtension)
            cv2.imwrite(filePath+filePathExtension, frame)
            images_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)))
            image_array = glob.glob(os.path.join(images_folder, filePath+filePathExtension))
            image = open(image_array[0], 'r+b')
           
            print(filePath+filePathExtension+ "***")
            faceDetect(img = image, fp = filePath+filePathExtension, counter = i)
            if(flag == True):
                i = i+1
        elif(cv2.waitKey(1) & 0xFF == ord('q')):
            print("$$$$$$goodbye$$$$$$")
            break

    return userName

def faceDetect(img, fp, counter):
    
    faces = face_client.face.detect_with_stream(img, return_face_id=True, return_face_landmarks=True, return_face_attributes=['age', 'gender', 'headPose', 'smile', 'facialHair', 'glasses', 'emotion'], recognition_model='recognition_02', return_recognition_model=False, detection_model='detection_01', custom_headers=None, raw=False, callback=None)
    
    if faces != []:
      rectanle = faces[0].face_rectangle
      if ((rectanle.height > 200) and (rectanle.width> 200)):
            #only keep picture if race rectangle is bigger than 200 x 200 (azure reccomends)
            counter+=1
            flag = True
            print("Number " + str(counter) + " Image saved *********")
      else: 
           print("***PLEASE COME NEAR THE CAMERA and RETAKE THE LAST PICTURE! ---- Image not saved ***** ")
           img.close()
           os.remove(fp)
           flag = False
    else:
        img.close()
        os.remove(fp)
    return None;        


def trainFaceGroup(userName):
    
    i=0;
    personGroupId = 'test' #### needs to be dynamic
    #creates new person in persongroup
    new_person = face_client.person_group_person.create(personGroupId, name= userName, user_data=None, recognition_model='recognition_02', custom_headers=None, raw=False)
    
    #assigns name of person in the persongroup

    new_person.name = userName
    print("TRAINFACEGROUP")
 
    # Find all jpeg images in working directory
    path = "/Users/risha/OneDrive/Desktop/visualStudio/"  #### needs to be dynamic
    os.chdir(path)
    

    imageList = [file for file in glob.glob('*.jpg') if file.startswith(userName)] ###STEP FOR RISHABBBBB
    print('Detected images: ',imageList)

    # Adds images to person in persongroup
    for image in imageList:
        imArray = open(image, 'r+b')
        face_client.person_group_person.add_face_from_stream(personGroupId, new_person.person_id, imArray)
    print("Training the person group for userName = " + userName)
    face_client.person_group.train(personGroupId)

    while (True):
        training_status = face_client.person_group.get_training_status(personGroupId)
        print("Training status: for userName = " + userName +"------> {} ".format(training_status.status) )
        if (training_status.status is TrainingStatusType.succeeded):
            break
        elif (training_status.status is TrainingStatusType.failed):
            sys.exit('No train for ' + userName)
       
    return



def main():

    #/Users/risha/OneDrive/Desktop/visualStudio/

   
   # name = captureImageFromVideo()
    #name = "rish"
    #trainFaceGroup(name)
    return
main()