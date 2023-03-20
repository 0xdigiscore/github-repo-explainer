# github.py
import requests
import os
import zipfile
from utils.http_utils import get_proxies
from env import GITHUB_TOKEN

API_BASE_URL = "https://api.github.com"

def download_repo_zip(user, repo, branch="main"):
    url = f"https://github.com/{user}/{repo}/archive/{branch}.zip"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    proxies = get_proxies()
    response = requests.get(url, headers=headers, proxies=proxies)

    if response.status_code != 200:
        raise Exception(f"Error downloading repository: {response.text}")

    zip_filename = f"{user}_{repo}_{branch}.zip"
    with open(zip_filename, "wb") as f:
        f.write(response.content)

    with zipfile.ZipFile(zip_filename, "r") as zip_ref:
        zip_ref.extractall()

    os.remove(zip_filename)

    print(f"Repository {user}/{repo} (branch {branch}) downloaded and extracted.")


def get_repo_contents_recursive(user, repo, path=""):
    url = f"{API_BASE_URL}/repos/{user}/{repo}/contents/{path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    proxies = get_proxies()
    response = requests.get(url, headers=headers, proxies=proxies)

    if response.status_code != 200:
        raise Exception(f"Error fetching contents of {user}/{repo}/{path}: {response.text}")

    contents = response.json()
    files = []

    for item in contents:
        if item["type"] == "file":
            files.append(item)
        elif item["type"] == "dir":
            files.extend(get_repo_contents_recursive(user, repo, item["path"]))

    return files

def download_file(url, destination_path):
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    proxies = get_proxies()
    response = requests.get(url, headers=headers, proxies=proxies)

    if response.status_code == 200:
        with open(destination_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded file to: {os.path.abspath(destination_path)}")
    else:
        raise Exception(f"Error downloading file: {response.text}")