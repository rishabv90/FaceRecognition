from tkinter import *

class createNew:
    def __init__(self):
        #self.master = master ?
        
        self._root = None #?


    def addUser(self):

        self._root = Tk()
        
        #root = Tk() ?

        #set size of window
        self._root.geometry("500x500") 
        
        #set the user input elements
        username = Label(self._root, text="Name: ")
        #password = Label(self._root, text="Password: ")
        #cfmPwd = Label(self._root, text="Confirm Password: ")
        entry_1 = Entry(self._root)
        #entry_2 = Entry(self._root)
        #entry_3 = Entry(self._root)
        username.grid(row=0, sticky=E) #sticky E = east, right aligned
        #password.grid(row=1, sticky=E)
        #cfmPwd.grid(row=2, sticky=E)
        entry_1.grid(row=0, column=1)
        #entry_2.grid(row=1, column=1)
        #entry_3.grid(row=2, column=1)
     
        #submit button
        b = Button(self._root, text="Submit")
        b.grid(columnspan=2)

        self._root.mainloop()
    #call the function to create a new page

