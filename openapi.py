# openapi.py
import requests

from env import OPENAPI_API_KEY

API_BASE_URL = "https://api.openapi.example.com"


def get_file_explanation(file_path):
    url = f"{API_BASE_URL}/explain"
    headers = {"Authorization": f"apiKey {OPENAPI_API_KEY}"}
    files = {"file": open(file_path, "rb")}

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Error getting explanation: {response.text}")
