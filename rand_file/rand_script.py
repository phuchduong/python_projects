base_dir = 'F:\\xDocuments\\xOther'

import os
from rand_file import rand_file

# Sets to the current folder path
current_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_path)


def get_rand_file():
    file_list = rand_file(base_dir)
    input("Press Enter for another file...")
    get_another_file(file_list)


def get_another_file(file_list):
    file_list.re_roll()
    input("Press Enter for another file...")
    get_another_file(file_list)

get_rand_file()
