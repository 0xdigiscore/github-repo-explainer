# config.py

import configparser

def load_config():
    config = configparser.ConfigParser()
    config.read("config.ini")

    github_token = config.get("github", "token")

    proxies = {}
    if config.has_section("proxy"):
        for protocol in ["http", "https"]:
            if config.has_option("proxy", protocol):
                proxies[protocol] = config.get("proxy", protocol)

    openapi_api_key = None
    if config.has_section("openapi"):
        if config.has_option("openapi", "api_key"):
            openapi_api_key = config.get("openapi", "api_key")

    download_dir = config.get("directories", "download_dir")
    output_dir = config.get("directories", "output_dir")

    return github_token, proxies, openapi_api_key, download_dir, output_dir
