import requests
from load_env import load_env
import os

load_env()
SLIDESPEAK_API_KEY = os.getenv("SLIDESPEAK_API_KEY")
url = "https://api.slidespeak.co/api/v1/presentation/generate"

headers = {
    "Content-Type": "application/json",
    "x-api-key": SLIDESPEAK_API_KEY
}