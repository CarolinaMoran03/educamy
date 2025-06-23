from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()


GENAI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GENAI_API_KEY)
modelName = 'gemini-1.5-flash-002'
model = genai.GenerativeModel(modelName)
print(f"GENAI_API_KEY: {GENAI_API_KEY}")


