# env.py
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENAPI_API_KEY = os.getenv("OPENAPI_API_KEY")
