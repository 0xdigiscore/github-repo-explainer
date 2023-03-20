# http_utils.py

from config.load_config import load_config

_, proxies, _, _,_ = load_config()

def get_proxies():
    return proxies
