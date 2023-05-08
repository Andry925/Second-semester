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
        self.label = tkinter.Label(self.frame, text="My program")
        self.label.pack()
        self.textentry = tkinter.Entry(self.frame)
        self.textentry.pack()
        self.button = tkinter.Button(self.frame, text="Click me")
        self.button.pack()

root = Interface()
root.mainloop()