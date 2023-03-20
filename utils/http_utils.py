# http_utils.py

import os

def get_proxies():
    return {
        "http": os.environ.get("HTTP_PROXY"),
        "https": os.environ.get("HTTPS_PROXY"),
    }
