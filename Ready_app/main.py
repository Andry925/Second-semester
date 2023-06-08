import os
import shutil
import time
import interface_with_file_manager
seconds_in_day = 86400
list_defect = ["$", ".lnk", ".LNK"]


class FileManager():

    def __init__(self):
        self.list_needed_extensions = []
        self.mainfolder_name = interface_with_file_manager.get_values()["mainfolder"]

        try:
            self.days = float(interface_with_file_manager.get_values()["days"]) * seconds_in_day
            self.needed_extensions = interface_with_file_manager.get_values()["extensions"]
            self.directory_to_store_files = interface_with_file_manager.get_values()["directory"]
            os.chdir(str(self.directory_to_store_files))
            self.path_to_start = interface_with_file_manager.get_values()["path"]

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

    def create_full_path(self, extension_for_full_path):
        for address, dirs, files in os.walk(self.path_to_start):

            for file in files:

                if extension_for_full_path in file:
                    full_path_to_file = os.path.join(address, file)
                    yield full_path_to_file

    def determine_defect_file(self,full_path_to_file):
        for defect in list_defect:
            if defect in full_path_to_file:
                return True

    def determine_time_interval(self,full_path_to_file):
        if time.time() - os.path.getctime(full_path_to_file) < self.days and not self.determine_defect_file(
            full_path_to_file):

            yield full_path_to_file

    def copy_to_extensions_folders(self, full_path_to_file):
        self.directory_to_copy_file = os.path.join(self.directory_to_store_files, self.mainfolder_name)
        for extension in self.list_needed_extensions:
            try:
                if extension in full_path_to_file:
                    destination_for_copied_file = os.path.join(self.directory_to_copy_file, extension)



                    shutil.copy(full_path_to_file, destination_for_copied_file)

            except BaseException:
                error_log_file = os.path.join(self.directory_to_copy_file, "mistakes.txt")
                with open(error_log_file, 'a') as file_mistake:
                    file_mistake.write(f"{full_path_to_file}\n")

    def run_code(self):
        for extension in self.create_extensions_folders(self.needed_extensions):

            for full_path_to_file in self.create_full_path(extension):
                for needed_extension in self.determine_time_interval(full_path_to_file):
                    self.copy_to_extensions_folders(needed_extension)
                    print(f"File is copied {full_path_to_file}")

    def final_decision(self):
        self.what_to_do = interface_with_file_manager.get_values()["final_decison"]
        if self.what_to_do == "Yes":
            shutil.rmtree(self.mainfolder_name)
