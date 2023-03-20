# main.py
import os
import sys

from github import download_repo_zip
from openapi import get_file_explanation
from utils.file_utils import create_directory_if_not_exists,find_py_files, get_output_path,get_repo_download_path

def main(user, repo, branch):
    download_repo_zip(user, repo, branch)

    repo_download_path = get_repo_download_path(user,repo,branch)
    files = find_py_files(repo_download_path)
    if not files:
        print(f"No Python files found in the {user}/{repo} repository.")
        return

    output_directory = get_output_path(user,repo,branch)
    create_directory_if_not_exists(output_directory)

    for code_file in files:
        file_name = os.path.basename(code_file)
        destination_path = os.path.join(output_directory, f"{os.path.splitext(file_name)[0]}.md")

        file_explanation = get_file_explanation(code_file)
        with open(destination_path, "w") as f:
            f.write(file_explanation)

        print(f"File {file_name} processed and explanation written to {destination_path}.")

    print(f"All Python files in {user}/{repo} processed successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <github_username> <repository_name>")
        sys.exit(1)

    user = sys.argv[1]
    repo = sys.argv[2]
    branch = sys.argv[3]

    main(user, repo, branch)
