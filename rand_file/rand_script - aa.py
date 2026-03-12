import os
from rand_file import RandFile

base_dir = 'V:\\aa_backup'
program = "C:\\Program Files (x86)\\K-Lite Codec Pack\\MPC-HC64\\mpc-hc64.exe"

# Sets to the current folder path
current_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_path)


def get_RandFile():
    file_list = RandFile(base_dir, program)
    input("Press Enter for another file...")
    get_another_file(file_list)


def get_another_file(file_list):
    file_list.re_roll()
    input("Press Enter for another file...")
    get_another_file(file_list)

get_RandFile()
