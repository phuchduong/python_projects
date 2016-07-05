import random
import os
import subprocess


class rand_file:

    def __init__(self, base_dir, program):
        self.base_dir = base_dir
        self.file_list = []
        self.program = program

        print("Building file list...")
        self.rbuild_file_list(self.base_dir)
        print("File list complete...")
        print(str(len(self.file_list)) + " files in list...")

        self.re_roll()

    def re_roll(self):
        print("Picking a random file from the list...")
        rand_file_str = random.choice(self.file_list)
        rand_file = rand_file_str.encode('utf-8')
        print(rand_file)
        # Opens the file
        subprocess.Popen([self.program, self.base_dir + rand_file_str])

    def rbuild_file_list(self, current_dir):
        dir_list = os.listdir(current_dir)
        for dir_name in dir_list:
            file_root = current_dir + "\\" + dir_name
            if os.path.isfile(file_root):
                # asbsolute to relative pathing
                relative_file_path = file_root.replace(self.base_dir, "")
                self.file_list.append(relative_file_path)
            elif os.path.isdir(file_root):
                self.rbuild_file_list(file_root)
            else:
                print("Invalid file state: " + str(file_root))
