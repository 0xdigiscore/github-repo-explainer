# github.py
import requests
import os

from env import GITHUB_TOKEN

API_BASE_URL = "https://api.github.com"

def get_repo_contents_recursive(user, repo, path=""):
    url = f"{API_BASE_URL}/repos/{user}/{repo}/contents/{path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)

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
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open(destination_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded file to: {os.path.abspath(destination_path)}")
    else:
        raise Exception(f"Error downloading file: {response.text}")