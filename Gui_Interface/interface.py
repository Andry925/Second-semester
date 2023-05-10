import tkinter

class Interface(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("An interface for my app")
        self.geometry("800x400")
        self.frame = tkinter.Frame(self)
        self.frame.pack()
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
        
root = Interface()
root.mainloop()