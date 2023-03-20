# GitHub Repository Python File Explainer

This project generates explanation Markdown files for Python files in a GitHub repository. It uses the GitHub API to fetch the files and OpenAPI SDK to generate the explanations.

## Prerequisites

1. Python 3.6 or higher
2. A GitHub Personal Access Token with repo access: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
3. An OpenAPI API Key: Replace this with instructions on how to get an API key for the OpenAPI SDK you are using.

## Setup

1. Clone this repository:
```
git clone https://github.com/yourusername/github-repo-python-file-explainer.git
cd github-repo-python-file-explainer
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory with the following content:
```
GITHUB_TOKEN=your_github_personal_access_token
OPENAPI_API_KEY=your_openapi_api_key
```

## Usage
```
python main.py <github_username> <repository_name>
```

Replace `<github_username>` and `<repository_name>` with the appropriate values for the GitHub repository you want to process. The program will download each Python file in the repository, generate a Markdown explanation using the OpenAPI SDK, and save the explanation in a folder named `<github_username>_<repository_name>_md_explanations`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
