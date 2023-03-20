# utils.py
import os

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def find_py_files(directory):
    py_files = []
    for subdir, _, files_list in os.walk(directory):
        for file in files_list:
            if file.endswith(".py"):
                py_files.append(os.path.join(subdir, file))
    return py_files