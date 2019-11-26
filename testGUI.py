from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk


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
                # Return a boolean success flag and the current frame converted to BGR
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
        self.btn_snapshot= Button(window, text="Snapshot", width=50, command=self.snapshot, bg="black", fg="white")
        self.btn_snapshot.pack(anchor=CENTER, expand=True)

        self.delay = 15
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

         if ret:
             cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

# Create a window and pass it to the Application object
root = Tk()
App(root, "Tkinter and OpenCV")