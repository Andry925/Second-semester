
import os 
import shutil
import time
class Parcer:
    def __init__(self):
       self.list_extension = []
       self.directory = input("Put the directore you want to store the file")
       os.chdir(self.directory)
       
       for file_path in self.search(input("Put the start"),input("Put the key you want to copy the file")):
           print(file_path)
        
    def search(self,path,key_for_search):
        self.key_for_search = key_for_search
        self.path = path
        for iteration in self.key_for_search.split():
            self.list_extension.append(iteration)
            self.y = f"mainfolder\{iteration}"
            os.makedirs(self.y)
    
        for adress,dirs,files in os.walk(self.path):
            for file in files:
                for second in self.key_for_search.split():
                    if second in file:

                        our_file =  os.path.join(adress,file)
                        if time.time() - os.path.getctime(our_file) < 2000000:
                            try:
                        
                                shutil.move(our_file,f"C:\Второй семестр\mainfolder\{second}")
                                yield our_file
                            except:
                                with open("C:\Второй семестр\mainfolder\mistakes.txt",'w') as file_mistake:
                                    file_mistake.write(our_file)
                            
                           
                               

                               
            
x = Parcer()

