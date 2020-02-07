from tkinter import *
from tkinter import ttk  
import PIL.Image, PIL.ImageTk

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
path = '/Users/Brian/source/repos/Face group/Face group/'

#To identify whether it is success or not


# Create a window and pass it to the Application object


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
            #print((time.time()-self.start_time))

            self.vid.release()
            
        #self.window.mainloop()
    def frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        else:
            return (ret, None)
    def get_frame(self):


        if self.vid.isOpened():
            fps = self.vid.get(cv2.CAP_PROP_FPS)

            ret, frame = self.vid.read()
            results = []
            if ret:
                cv2.imwrite(path + "frame" + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                # Return a boolean success flag and the current frame converted to BGR
                IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)))
                group_photo ='frame.jpg'
                # Get test image
                test_image_array = glob.glob(os.path.join(IMAGES_FOLDER, group_photo))
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
                if not results:
                    #print('No person identified in the person group'.format(os.path.basename(image.name)))
                    variable.set('No person identified in the person group')
                    #global f
                    #f.quit()

                for person in results:
                    if person.candidates != []:
                   
                    
                        #.get() used to return person object in persongroup
                        try:
                            temp = face_client.person_group_person.get(PERSON_GROUP_ID, person.candidates[0].person_id, custom_headers=None, raw=False)
                        
                        except:
                            print('Not in database')
                            break

                        names.append(temp.name)
                        confidence.append(person.candidates[0].confidence)
                        #print('Person: {}    Confidence: {}.'.format(temp.name, person.candidates[0].confidence)) # Get topmost confidence score
                    else:
                    
                        results.remove(person)
                   
        
                faces = faces[:len(results)] #trim faces to match length of results
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
                            variable.set('Logging in: ' + names[count] + ' identified as ' + str(face_attributes.age) + 
                                         ' years old and with ' + face_attributes.glasses)
                            print(temp.user_data)

                            data = temp.user_data.split(',')
                            
                            newData = datetime.now().strftime('%m/%d/%Y, %H:%M:%S') + ',' + data[-1]


                            face_client.person_group_person.update(PERSON_GROUP_ID,temp.person_id,user_data = newData)
                            success.set('True')
                        else:
                            color = (0,0,150)
                            variable.set('Not logging in, but found similar, so try to move closer or give better lighting')

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
                        image.close()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                image.close()

                return (ret, None)
        else:
            return (ret, None)

class createNew:
    def __init__(self):
        self._root = Tk()
        self._root.geometry("1400x900")

        self._vid = MyVideoCapture(video_source=0)
        self._n = StringVar()
        self._type = StringVar()

        self._canvas = Canvas(self._root, width = self._vid.width, height = self._vid.height)
        self._canvas.grid(row = 0, column = 1)

        framee = Frame(self._root)
        framee.grid(row = 0,column =0)
        
        nameLable = Label(framee, text="User Type: ").grid(row = 0,column =0,sticky = 'W',pady = 5)

        dropMenu = OptionMenu(framee,self._type,'Admin','User').grid(row = 0,column =1,pady = 5)

        

        self._i = 1
        nameLable2 = Label(framee, text="Name: ").grid(row = 1,column =0,sticky = 'W',pady = 5)
       
        nameEntry = Entry(framee,textvariable = self._n).grid(row = 1,column = 1,pady = 5)

        
        b = Button(framee, text="Submit",fg="white", bg="black", command=self.addUser).grid(row = 2, column =1,pady = 5)

        self._root.mainloop()
        return

        
        
    def addUser(self):
        Name = self._n.get()
        if self._i < 5:
            ret, frame = self._vid.frame()
            self._photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self._canvas.create_image(0, 0, image = self._photo,anchor = NW)
            
            file_name = path + Name + str(self._i) + '.jpg'

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

            del self._vid
            self.azure()
            return

        self._root.after(10,self.addUser)
        return
            
    def azure(self):
        Name = self._n.get()
        data = ''
        t = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
        data = t + ',' + self._type.get()
        print(data)
        new_person = face_client.person_group_person.create(PERSON_GROUP_ID, name= Name, user_data=data, custom_headers=None, raw=False)
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
                self._root.destroy()
                return
            elif (training_status.status is TrainingStatusType.failed):
                sys.exit('Training the person group has failed.')
        return
    
class deleteUser:
    def __init__(self):
        self._root = Tk()
        self._root.geometry("800x500+700+300")
        self._tree = ttk.Treeview(self._root,columns = ('#1','#2','#3','#4'))
        self._tree.configure(selectmode = "extended")
        self._tree.heading('#0',text = 'Name: ')
        self._tree.heading('#1',text = 'Person ID: ')
        self._tree.heading('#2',text = 'Date: ')
        self._tree.heading('#3',text = 'Time: ')
        self._tree.heading('#4',text = 'Account Type: ')


        self._tree.column('#0',anchor = 'center', width = 100)
        self._tree.column('#1', anchor = 'center',width = 250)
        self._tree.column('#2',anchor = 'center', width = 100)
        self._tree.column('#3',anchor = 'center', width = 100)
        self._tree.column('#4',anchor = 'center', width = 100)
        person_groups = face_client.person_group.list(start=None, top=1000, return_recognition_model=False, custom_headers=None, raw=False)
        dic = {}

        for PersonGroupObj in person_groups:
            dic[PersonGroupObj.name] = []

            people = face_client.person_group_person.list(PersonGroupObj.name, start=None, top=None, custom_headers=None, raw=False)
            for p in people:
                data = p.user_data.split(',')
                print(data)
                dic[PersonGroupObj.name].append([p.name,p.person_id,data[0],data[1],data[2]])
        print(dic)
        keys= list(dic.keys())  
        print(keys)
        for i in range(0,len(dic[keys[0]])):
            print(dic[keys[0]][i][0])
            self._tree.insert('','0','item' + str(i), text = dic[keys[0]][i][0], values = (dic[keys[0]][i][1],dic[keys[0]][i][2],dic[keys[0]][i][3],dic[keys[0]][i][4]))
           

        self._tree.pack()
        selectionB = Button(self._root,text = 'Select',command = self.selections)
        selectionB.pack()
        self._root.mainloop()

        return
   

        
        
    def selections(self):
       
        for el in self._tree.selection():
            info = self._tree.item(el)

            person_group_id = 'test'
            person_id = info['values'][0]
            face_client.person_group_person.delete(person_group_id, person_id, custom_headers=None, raw=False)        
        self._root.destroy() 
           
        return
    

class App:
    def __init__(self, window, window_title,frame,var,success, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        root.bind('<Escape>', lambda e: root.destroy())

            
        #Add frame within window
        self._f = frame
    
        #Containers
        leftFrame = Frame(f)
        leftFrame.pack(side=LEFT)
        bottomFrame = Frame(f)
        bottomFrame.pack(side=BOTTOM)
        rightFrame = Frame(f)
        rightFrame.pack(side=RIGHT)
        

        #open video source

        self.vid = MyVideoCapture(video_source)
        #create a canvas that can fit the above video source size
        self.canvas = Canvas(f, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        #Text showing log in status
        self._variable = var

        self._success = success

        #variable.set(statusString)
        status = Label(bottomFrame, bd=1, relief=SUNKEN, anchor=W,
                      textvariable=self._variable, width=100, fg="gray19", bg='ivory3')
        status.pack()        

        menu = Menu(self.window)
        self.window.config(menu = menu)
        submenu = Menu(menu,tearoff=0)

        menu.add_cascade(label = 'Menu',menu = submenu)
        submenu.add_command(label = 'Add User',command = self.directNew)
        submenu.add_command(label = 'Delete User', command = self.directDelete)
     
        self.delay = 10
        self.update()
        
        self.window.mainloop()
    
    def update(self):
        #print('success: %s' % success)
        if self._success.get() == 'False':
            #Get a frame from the video source
            ret, frame = self.vid.get_frame()
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
            self.window.after(self.delay, self.update)
        else:
            del self.vid

        
            
    def directNew(self):
    
        self.window.destroy()

        obj = createNew()

        return 
    def directDelete(self):
        

        self.window.destroy()
        
        obj = deleteUser()
        return 


while True:

    root = Tk()
    variable = StringVar()
    success = StringVar()
    success.set('False')
    f = Frame(root)
    f.pack()

    root.geometry("800x500+700+300")
    App(root, "Facial Recognition",frame = f,var = variable,success = success)
