# main.py
import os
import sys

from github import download_repo_zip, get_repo_contents_recursive, download_file
from openapi import get_file_explanation
from utils.file_utils import create_directory_if_not_exists

def main(user, repo, branch):
    download_repo_zip(user, repo, branch)

    files = []
    for subdir, _, files_list in os.walk(repo):
        for file in files_list:
            if file.endswith(".py"):
                files.append(os.path.join(subdir, file))

    if not files:
        print(f"No Python files found in the {user}/{repo} repository.")
        return

    output_directory = f"{user}_{repo}_md_explanations"
    create_directory_if_not_exists(output_directory)

    for code_file in files:
        file_name = os.path.basename(code_file)
        file_url = f"file://{os.path.abspath(code_file)}"
        destination_path = os.path.join(output_directory, f"{os.path.splitext(file_name)[0]}.md")

        file_explanation = get_file_explanation(code_file)
        with open(destination_path, "w") as f:
            f.write(file_explanation)

        print(f"File {file_name} processed and explanation written to {destination_path}.")

    print(f"All Python files in {user}/{repo} processed successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <github_username> <repository_name>")
        sys.exit(1)

    user = sys.argv[1]
    repo = sys.argv[2]
    branch = sys.argv[3]

    main(user, repo, branch)
