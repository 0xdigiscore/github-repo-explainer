# openapi.py
import requests

from env import OPENAPI_API_KEY
from utils.http_utils import get_proxies

API_BASE_URL = "https://api.openapi.example.com"


def get_file_explanation(file_path):
    url = f"{API_BASE_URL}/explain"
    headers = {"Authorization": f"apiKey {OPENAPI_API_KEY}"}
    files = {"file": open(file_path, "rb")}
    
    proxies = get_proxies()
    response = requests.post(url, headers=headers,files=files, proxies=proxies)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Error getting explanation: {response.text}")
