# utils.py
import os
from config.load_config import load_config

_, proxies, _, download_dir,output_dir = load_config()

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

def get_repo_download_path(user, repo, branch):
    return f"{download_dir}/{user}_{repo}_{branch}"

def get_output_path(user,repo,branch):
    return f"{output_dir}/{user}_{repo}_{branch}_md_explanations"

