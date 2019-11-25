
import asyncio, io, glob, os, sys, time, uuid, requests, cv2
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType

 

# Set the FACE_SUBSCRIPTION_KEY environment variable with your key as the value.
# This key will serve all examples in this document.
global KEY
KEY = '12f952f3b226421aa2019ab14740b123'
# Set the FACE_ENDPOINT environment variable with the endpoint from your Face service in Azure.
# This endpoint will be used in all examples in this quickstart.
global ENDPOINT
ENDPOINT = "https://testface19025.cognitiveservices.azure.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=true&returnFaceAttributes=[age,gender,glasses]&recognitionModel=recognition_02&returnRecognitionModel=false&detectionModel=detection_01"

global face_client
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

while True:
    person_groups = face_client.person_group.list(start=None, top=1000, return_recognition_model=False, custom_headers=None, raw=False)
    dic = {}

    for PersonGroupObj in person_groups:
        dic[PersonGroupObj.name] = []

        people = face_client.person_group_person.list(PersonGroupObj.name, start=None, top=None, custom_headers=None, raw=False)
        for p in people:
            dic[PersonGroupObj.name].append([p.name,p.person_id])

    keys = list(dic.keys())


    if input('Do you want to delete a person group? (Y/N)').lower() == 'y':
        i = 1
        for key in keys:
            print(str(i) + '. ' + key)
            i+=1
        num = input("Enter the number for the corresponding person group that you want to delete: ")
        num = int(num) - 1
        person_group_id = keys[num]
        face_client.person_group.delete(person_group_id, custom_headers=None, raw=False)
        print('Deleted person_group_id: ',person_group_id)

    else:
        i = 1
        for key in keys:
            print(str(i) + '. ' + key)
            i+=1
        num = input("Enter the number for the corresponding person group that you want to delete a person from: ")
        print()
        num = int(num) - 1
        i = 1
        print('People')
        for p in dic[keys[num]]:
            print(str(i) + '. ' + p[0])
            i += 1
        num2 = input("Enter the number for the person you want to delte: ")
        num2 = int(num2) - 1
        person_group_id = keys[num2]
        person_id = p[1]
        face_client.person_group_person.delete(person_group_id, person_id, custom_headers=None, raw=False)
        print('Deleted')
        
