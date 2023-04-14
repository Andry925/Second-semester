import tkinter
import sys
import os
import shutil
import time
seconds_in_day = 86400

class FileManager():
    def __init__(self):
        self.list_extension = []
        self.name_folder = input("How would you call mainfolder")
        while True:
            try:
                self.day = float(
                    input("Put the time interval in days -")) * seconds_in_day
                self.directory = input(
                    "Put the directore you want to store the file -")
                os.chdir(self.directory)
                self.way = input("Put the path -")
                break
            except :
                print("Invalid input of data -")
        self.extension_folders(self.directory, input("Put extensions -"))
        for file in self.create_full_path():
            self.sort_and_move(file)
            print(f"File is copied {file}")
        self.final_decision()

    def extension_folders(self, path, extension_for_search):
        self.extension_for_search = extension_for_search
        self.path = path
        for extension in self.extension_for_search.split():
            self.list_extension.append(extension)
            self.mainfolder = f"{self.name_folder}\\{extension}"
            os.makedirs(self.mainfolder)
        

    def create_full_path(self):
        self.list_defect = ["$",".lnk",".LNK"]
        self.path_copy = os.path.join(self.directory, self.name_folder)
        for adress, dirs, files in os.walk(self.way):

            for file in files:
                for extension_copy in self.extension_for_search.split():
                    if extension_copy in file and not any(defect in our_file for defect in self.list_defect):
                        our_file = os.path.join(adress, file)
                        if time.time() - os.path.getctime(our_file) < self.day:
                           
                            
                            yield our_file

    def sort_and_move(self, our_file):
        for extension in self.list_extension:
            try:
                if extension in our_file:
                    shutil.copy(our_file, os.path.join(self.path_copy, extension))
                    

            except :
                with open(os.path.join(self.path_copy, "mistakes.txt"), 'a') as file_mistake:
                    file_mistake.write(f"{our_file}\n")

    def final_decision(self):
        self.what_to_do = input("Do you want to delete these files -")
        if self.what_to_do == "Yes":
            shutil.rmtree(self.name_folder)



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
        self.label = tkinter.Label(self.window,text = "My program")
        self.label.pack()
        self.button = tkinter.Button(self.window,text = "Click me",command= FileManager)
        self.button.pack()
     



        
root = Interface()
root.mainloop()



