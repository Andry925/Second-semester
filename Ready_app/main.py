import interface_with_file_manager
import os
import shutil
import time
seconds_in_day = 86400
list_defect = ["$", ".lnk", ".LNK"]


class FileManager():
    
    def __init__(self):
        self.list_needed_extensions = []
        self.mainfolder_name = interface_with_file_manager.get_mainfolder()
       
        try:
            self.days = int(
            interface_with_file_manager.get_days()) * seconds_in_day
            self.needed_extensions = interface_with_file_manager.get_extensions()
            self.directory_to_store_files = interface_with_file_manager.get_directory()
            os.chdir(str(self.directory_to_store_files))
            self.path_to_start = interface_with_file_manager.get_way()
       
        except BaseException:
                print("Invalid input of data -")
        self.run_code()
        self.final_decision()
        

    def create_extensions_folders(self, needed_extensions):
        self.needed_extensions = needed_extensions
        for extension in self.needed_extensions.split():
            self.list_needed_extensions.append(extension)
            self.extension_folders_in_mainfolder = f"{self.mainfolder_name}\\{extension}"
            os.makedirs(self.extension_folders_in_mainfolder)
            yield extension




    def create_full_path(self,extension_for_full_path):
        for address, dirs, files in os.walk(self.path_to_start):

            for file in files:

                if extension_for_full_path in file:
                     full_path_to_file = os.path.join(address, file)
                     if time.time() - os.path.getctime(full_path_to_file) < self.days and not any(
                         defect in full_path_to_file for defect in list_defect):

                        yield full_path_to_file


    

    def copy_to_extensions_folders(self, full_path_to_file):
        self.path_to_copy_file = os.path.join(self.directory_to_store_files, self.mainfolder_name)
        for extension in self.list_needed_extensions:
            try:
                if extension in full_path_to_file:
                    shutil.copy(
                        full_path_to_file, os.path.join(
                            self.path_to_copy_file, extension))

            except BaseException:
                with open(os.path.join(self.path_to_copy_file, "mistakes.txt"), 'a') as file_mistake:
                    file_mistake.write(f"{full_path_to_file}\n")
    
    def run_code(self):
         for extension in self.create_extensions_folders(self.needed_extensions):

            for full_path_to_file in self.create_full_path(extension):
                self.copy_to_extensions_folders(full_path_to_file)
                print(f"File is copied {full_path_to_file}")

    
    def final_decision(self):
        self.what_to_do = interface_with_file_manager.get_final_decision()
        if self.what_to_do == "Yes":
            shutil.rmtree(self.mainfolder_name)



