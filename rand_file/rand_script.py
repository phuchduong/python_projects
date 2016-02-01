base_dir = 'E:\\xDocuments\\xOther'

import os

# Sets to the current folder path
current_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_path)

from rand_file import rand_file

file_tree = rand_file(base_dir)