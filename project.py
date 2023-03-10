import os 
import shutil
import time
class Parcer:
    def __init__(self):
      
       self.list_iteration = []
       self.x = input("Put the directore you want to store the file")
       os.chdir(self.x)
       
       for run in self.search(input("Put the start"),input("Put the key you want to copy the file")):
           print(run)
        
    def search(self,path,key_for_search):
        self.key_for_search = key_for_search
        self.path = path
        for iteration in self.key_for_search.split():
            self.list_iteration.append(iteration)
            self.y = f"mainfolder\{iteration}"
            os.makedirs(self.y)
    
        for adress,dirs,files in os.walk(self.path):
            for file in files:
                if self.key_for_search in file:

                    our_file =  os.path.join(adress,file)
                    if time.time() - os.path.getctime(our_file) < 864000:
                        
                        shutil.copy(our_file,os.path.join(self.x,self.y))
                        yield our_file
                            
                           
                               

                               
            
x = Parcer()

