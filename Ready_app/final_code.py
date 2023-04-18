from project import FileManager
import tkinter


class Interface(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.window = tkinter.Tk()
        self.create_window()
        self.create_widgets()
    
    def create_window(self):
        self.window.title("An interface for my app")
        self.window.geometry("800x400")
        self.frame = tkinter.Frame(self.window)
        self.frame.pack()

    
    
    def create_widgets(self):
        self.label = tkinter.Label(self.frame,text = "My program")
        self.label.pack()
        self.textentry = tkinter.Entry(self.frame)
        self.textentry.pack()
        self.button = tkinter.Button(self.frame,text = "Click me",command = FileManager)
        self.button.pack()
       
        
root = Interface()
root.mainloop()