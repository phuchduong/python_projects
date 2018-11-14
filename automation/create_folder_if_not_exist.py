def create_data_folder_if_not_exist(data_folder_name):
    # Creates a folder if it does not already exist.
    # Takes in a folder name. Creates it in the current working directory.
    # Returns the full path of the folder.
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    data_folder_path = os.path.join(cur_dir, data_folder_name)
    if not os.path.exists(data_folder_path):
        os.makedirs(data_folder_path)
        print('Created a directory: ' + data_folder_path)
    return data_folder_path
