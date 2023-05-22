import tkinter


class Interface(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("An interface for my app")
        self.geometry("300x300")
        self.resizable(height=False, width=False)
        self.frame = tkinter.Frame(self)
        self.frame.grid()
        self.create_labels()
        self.create_entry()
        self.pack_widgets()
        self.final_decision_option()
        self.create_button()

    def create_labels(self):

        self.label_mainfolder = tkinter.Label(self.frame, text="How would you call mainfolder")
        self.label_days = tkinter.Label(self.frame, text="Put the time interval in days")
        self.label_extensions = tkinter.Label(self.frame, text="Put the extensions you need")
        self.label_directory = tkinter.Label(self.frame, text="Put the directory you want to store the file")
        self.label_path = tkinter.Label(self.frame, text="Put the path to start with")

    def create_entry(self):
        self.textentry_mainfolder = tkinter.Entry(self.frame)
        self.textentry_days = tkinter.Entry(self.frame)
        self.textentry_extensions = tkinter.Entry(self.frame)
        self.textentry_directory = tkinter.Entry(self.frame)
        self.textentry_path = tkinter.Entry(self.frame)

    def pack_widgets(self):
        self.label_mainfolder.grid()
        self.textentry_mainfolder.grid()
        self.label_days.grid()
        self.textentry_days.grid()
        self.label_extensions.grid()
        self.textentry_extensions.grid()
        self.label_directory.grid()
        self.textentry_directory.grid()
        self.label_path.grid()
        self.textentry_path.grid()

    def create_button(self):
        self.button = tkinter.Button(self.frame, text="Run code")
        self.button.grid()

    def final_decision_option(self):
        self.label_decison = tkinter.Label(
            self.frame, text="Do you want to delete these files ?")
        self.textentry_option = tkinter.Entry(self.frame)
        self.label_decison.grid()
        self.textentry_option.grid()


root = Interface()


root.mainloop()
