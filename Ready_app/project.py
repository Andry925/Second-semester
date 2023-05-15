import final_code
import os
import shutil
import time
seconds_in_day = 86400
list_defect = ["$", ".lnk", ".LNK"]


class FileManager():
    def __init__(self):
        self.list_extension = []
        self.name_folder = final_code.get_mainfolder()
       
        try:
            self.day = int(
            final_code.get_days()) * seconds_in_day
            self.extension_for_search = final_code.get_extensions()
            self.directory = final_code.get_directory()
            os.chdir(str(self.directory))
            self.way = final_code.get_way()
       
        except BaseException:
                print("Invalid input of data -")
        self.run_code()
        self.final_decision()

    def extension_folders(self, extension_for_search):
        self.extension_for_search = extension_for_search
        for extension in self.extension_for_search.split():
            self.list_extension.append(extension)
            self.mainfolder = f"{self.name_folder}\\{extension}"
            os.makedirs(self.mainfolder)
            yield extension


    def create_full_path(self,extension_copy):
        for address, dirs, files in os.walk(self.way):

            for file in files:

                if extension_copy in file:
                     our_file = os.path.join(address, file)
                     if time.time() - os.path.getctime(our_file) < self.day and not any(
                         defect in our_file for defect in list_defect):

                        yield our_file

    def sort_and_move(self, our_file):
        self.path_copy = os.path.join(self.directory, self.name_folder)
        for extension in self.list_extension:
            try:
                if extension in our_file:
                    shutil.copy(
                        our_file, os.path.join(
                            self.path_copy, extension))

            except BaseException:
                with open(os.path.join(self.path_copy, "mistakes.txt"), 'a') as file_mistake:
                    file_mistake.write(f"{our_file}\n")
    
    def run_code(self):
         for extension in self.extension_folders(self.extension_for_search):

            for file in self.create_full_path(extension):
                self.sort_and_move(file)
                print(f"File is copied{file}")

    
    def final_decision(self):
        self.what_to_do = input("Do you want to delete these files")
        if self.what_to_do == "Yes":
            shutil.rmtree(self.name_folder)



