from tkinter import Tk
import os 
import shutil
import time
class File_manager(Tk):
    def __init__(self):
       self.list_extension = []
       seconds_in_day = 86400
       self.day = float(input("Put the time interval in days")) * 86400
       self.directory = input("Put the directore you want to store the file")
       os.chdir(self.directory)
       self.extension_folders(input("Put the start"),input("Put the extension"))
       for file_path in self.search(self.path,self.extension_for_search):
           print(file_path)
        
    def extension_folders(self,path,extension_for_search):
        self.extension_for_search = extension_for_search
        self.path = path
        for extension in self.extension_for_search.split():
            self.list_extension.append(extension)
            self.mainfolder = f"mainfolder\{extension}"
            os.makedirs(self.mainfolder)
        return self.path, self.extension_for_search

    def search(self,path,key_for_search):
        for adress,dirs,files in os.walk(self.path):
            self.path_copy = os.path.join(self.directory,"mainfolder")
            for file in files:
                for extension_copy in self.extension_for_search.split():
                    if extension_copy in file:

                        our_file =  os.path.join(adress,file)
                        if time.time() - os.path.getctime(our_file) < self.day and "$"  not in our_file:
                            try:
                        
                                shutil.move(our_file,os.path.join(self.path_copy,extension_copy))
                                yield our_file
                            except:
                                with open(os.path.join(self.path_copy,"mistakes.txt"),'w') as file_mistake:
                                    file_mistake.write(our_file)
                               
                            
x = File_manager()

while True:
    what_to_do = input("Do you want to delete these files ?")
    if what_to_do == "Yes":
        shutil.rmtree("mainfolder")
        break
    else:
        break
