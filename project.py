from tkinter import Tk
import sys
import os 
import shutil
import time
name_folder = input("How would you call mainfolder")
class File_manager(Tk):
    def __init__(self):
       self.list_extension = []
       seconds_in_day = 86400
       while True:
           try:
               self.day = float(input("Put the time interval in days")) * seconds_in_day
               self.directory = input("Put the directore you want to store the file")
               os.chdir(self.directory)
               self.way = input("Put the path")
               break
           except:
               print("Invalid input of data")
       self.extension_folders(self.directory,input("Put extensions"))
       for file in self.create_full_path(self.way,self.extension_for_search):
           self.sort_and_move(self.directory,file)
           print(f"File is copied{file}")

    def extension_folders(self,path,extension_for_search):
        self.extension_for_search = extension_for_search
        self.path = path
        for extension in self.extension_for_search.split():
            self.list_extension.append(extension)
            self.mainfolder = f"{name_folder}\{extension}"
            os.makedirs(self.mainfolder)
        return self.path, self.extension_for_search

    def create_full_path(self,path,key_for_search):
        self.path_copy = os.path.join(self.directory,name_folder)
        for adress,dirs,files in os.walk(self.way):
            
            for file in files:
                for extension_copy in self.extension_for_search.split():
                    if extension_copy in file:
                        our_file =  os.path.join(adress,file)
                        if time.time() - os.path.getctime(our_file) < self.day and "$" not in our_file :
                            print(sys.getsizeof(our_file))
                            yield our_file
                        
    def sort_and_move(self,path,our_file):
       for extension in self.list_extension:
            try:
                shutil.copy(our_file,os.path.join(self.path_copy,extension))
                time.sleep(0.1)
                
            except:
                with open(os.path.join(self.path_copy,"mistakes.txt"),'w') as file_mistake:
                    file_mistake.write(our_file)
run = File_manager()
while True:
    what_to_do = input("Do you want to delete these files ?")
    if what_to_do == "Yes":
        shutil.rmtree(name_folder)
        break
    else:
        break
