from dotenv import load_dotenv
import os

load_dotenv()

print(f"SLIDESPEAK: {os.getenv('SLIDESPEAK_API_KEY')}")
