import final_code
import os
import shutil
import time
seconds_in_day = 86400
list_defect = ["$", ".lnk", ".LNK"]


class FileManager():
    
    def __init__(self):
        self.list_needed_extensions = []
        self.mainfolder_name = final_code.get_mainfolder()
       
        try:
            self.days = int(
            final_code.get_days()) * seconds_in_day
            self.needed_extensions = final_code.get_extensions()
            self.directory_to_store_files = final_code.get_directory()
            os.chdir(str(self.directory_to_store_files))
            self.path_to_start = final_code.get_way()
       
        except BaseException:
                print("Invalid input of data -")
        self.run_code()
        self.final_decision()
        

    def create_extension_folders(self, needed_extensions):
        self.needed_extensions = needed_extensions
        for extension in self.needed_extensions.split():
            self.list_needed_extensions.append(extension)
            self.extension_folders_in_mainfolder = f"{self.mainfolder_name}\\{extension}"
            os.makedirs(self.extension_folders_in_mainfolder)
            yield extension




    def create_full_path(self,extension_copy):
        for address, dirs, files in os.walk(self.path_to_start):

            for file in files:

                if extension_copy in file:
                     our_file = os.path.join(address, file)
                     if time.time() - os.path.getctime(our_file) < self.days and not any(
                         defect in our_file for defect in list_defect):

                        yield our_file

    def sort_and_move(self, our_file):
        self.path_copy = os.path.join(self.directory_to_store_files, self.mainfolder_name)
        for extension in self.list_needed_extensions:
            try:
                if extension in our_file:
                    shutil.copy(
                        our_file, os.path.join(
                            self.path_copy, extension))

            except BaseException:
                with open(os.path.join(self.path_copy, "mistakes.txt"), 'a') as file_mistake:
                    file_mistake.write(f"{our_file}\n")
    
    def run_code(self):
         for extension in self.create_extension_folders(self.needed_extensions):

            for file in self.create_full_path(extension):
                self.sort_and_move(file)
                print(f"File is copied {file}")

    
    def final_decision(self):
        self.what_to_do = final_code.get_final_decision()
        if self.what_to_do == "Yes":
            shutil.rmtree(self.mainfolder_name)



