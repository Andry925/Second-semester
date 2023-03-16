
import os 
import shutil
import time
class Parcer:
    def __init__(self):
       self.list_extension = []
       seconds_in_day = 86400
       self.day = int(input("Put the time interval in days")) * 86400
       self.directory = input("Put the directore you want to store the file")
       os.chdir(self.directory)
       self.extension_folders(input("Put the start"),input("Put the extension"))
       
       
       for file_path in self.search(self.path,self.key_for_search):
          
           
           print(file_path)
        
    def extension_folders(self,path,key_for_search):
        self.key_for_search = key_for_search
        self.path = path
        for extension in self.key_for_search.split():
            self.list_extension.append(extension)
            self.mainfolder = f"mainfolder\{extension}"
            os.makedirs(self.mainfolder)
        return self.path, self.key_for_search

        
    
    def search(self,path,key_for_search):
        for adress,dirs,files in os.walk(self.path):
            self.path_copy = os.path.join(self.directory,"mainfolder")
            for file in files:
                for extension_copy in self.key_for_search.split():
                    if extension_copy in file:

                        our_file =  os.path.join(adress,file)
                        if time.time() - os.path.getctime(our_file) < self.day and "$" not in our_file:
                            try:
                        
                                shutil.copy(our_file,os.path.join(self.path_copy,extension_copy))
                                yield our_file
                            except:
                                with open(os.path.join(self.path_copy,"mistakes.txt"),'w') as file_mistake:
                                    file_mistake.write(our_file)
                            
                           
                               

                               
            
x = Parcer()

