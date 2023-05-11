import tkinter

class Interface(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("An interface for my app")
        self.geometry("300x300")
        self.frame = tkinter.Frame(self)
        self.frame.grid()
        self.create_widgets()
        

    def create_widgets(self):
       
        self.label_mainfolder = tkinter.Label(self.frame, text="How would you call mainfolder")
        self.label_mainfolder.grid()
        self.textentry_mainfolder = tkinter.Entry(self.frame)
        self.textentry_mainfolder.grid()
        self.label_days = tkinter.Label(self.frame, text="Put the time interval in days ")
        self.label_days.grid()
        self.textentry_days = tkinter.Entry(self.frame)
        self.textentry_days.grid()
        self.label_extensions = tkinter.Label(self.frame, text="Put the extensdions you need")
        self.label_extensions.grid()
        self.textentry_extensions = tkinter.Entry(self.frame)
        self.textentry_extensions.grid()
        self.directory = tkinter.Label(self.frame, text="Put the directory you want to store the file")
        self.directory.grid()
        self.directory = tkinter.Entry(self.frame)
        self.directory.grid()
        self.path = tkinter.Label(self.frame, text="Put the path to start with")
        self.path.grid()
        self.path= tkinter.Entry(self.frame)
        self.path.grid()
        self.button = tkinter.Button(self.frame,text = "Run code")
        self.button.grid()
        
root = Interface()
root.mainloop()