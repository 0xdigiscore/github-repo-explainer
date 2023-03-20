# main.py
import os
import sys

from github import get_repo_contents_recursive, download_file
from openapi import get_file_explanation
from utils.file_utils import create_directory_if_not_exists

def main(user, repo):
    contents = get_repo_contents_recursive(user, repo)
    code_files = [item for item in contents if item["name"].endswith(".py")]

    if not code_files:
        print(f"No Python files found in the {user}/{repo} repository.")
        return

    temp_directory = "temp"
    create_directory_if_not_exists(temp_directory)

    output_directory = f"{user}_{repo}_md_explanations"
    create_directory_if_not_exists(output_directory)

    for code_file in code_files:
        print(f"Downloading {code_file['path']}...")
        temp_file_path = os.path.join(temp_directory, code_file["path"])
        temp_file_directory = os.path.dirname(temp_file_path)
        create_directory_if_not_exists(temp_file_directory)

        download_file(code_file["download_url"], temp_file_path)
        print(f"Downloaded {code_file['path']}.")

        if not os.path.isfile(temp_file_path):
            print(f"{temp_file_path} not found after downloading {code_file['path']}.")
            continue

        explanation = get_file_explanation(temp_file_path)

        md_file_path = os.path.join(output_directory, f"{code_file['path']}.md")
        md_file_directory = os.path.dirname(md_file_path)
        create_directory_if_not_exists(md_file_directory)

        with open(md_file_path, "w") as md_file:
            md_file.write(explanation)

        os.remove(temp_file_path)
        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <github_username> <repository_name>")
        sys.exit(1)

    user = sys.argv[1]
    repo = sys.argv[2]

    main(user, repo)
