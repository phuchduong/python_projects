import os
from rand_file import rand_file

base_dir = 'E:\\Unreconciled\\xOther'
program = "C:\\Program Files\\Combined Community Codec Pack 64bit\\MPC\\mpc-hc64.exe"

# Sets to the current folder path
current_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_path)


def get_rand_file():
    file_list = rand_file(base_dir, program)
    input("Press Enter for another file...")
    get_another_file(file_list)


def get_another_file(file_list):
    file_list.re_roll()
    input("Press Enter for another file...")
    get_another_file(file_list)


os.startfile('K:\\IOmega\\bt2')
get_rand_file()
