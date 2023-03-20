# main.py
import os
import sys

from github import download_repo_zip, get_repo_contents_recursive, download_file
from openapi import get_file_explanation
from utils.file_utils import create_directory_if_not_exists

def main(user, repo):
    download_repo_zip(user, repo)

    contents = get_repo_contents_recursive(user, repo)
    code_files = [item for item in contents if item["name"].endswith(".py")]

    if not code_files:
        print(f"No Python files found in the {user}/{repo} repository.")
        return

    output_directory = f"{user}_{repo}_md_explanations"
    create_directory_if_not_exists(output_directory)

    for code_file in code_files:
        file_url = code_file["download_url"]
        file_name = code_file["name"]
        destination_path = os.path.join(output_directory, f"{os.path.splitext(file_name)[0]}.md")

        download_file(file_url, file_name)
        file_explanation = get_file_explanation(file_name)
        with open(destination_path, "w") as f:
            f.write(file_explanation)

        os.remove(file_name)

        print(f"File {file_name} processed and explanation written to {destination_path}.")

    print(f"All Python files in {user}/{repo} processed successfully.")
        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <github_username> <repository_name>")
        sys.exit(1)

    user = sys.argv[1]
    repo = sys.argv[2]

    main(user, repo)
