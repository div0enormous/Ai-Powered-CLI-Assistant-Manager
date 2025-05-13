import json
import os
import requests

# Constants
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
API_KEY_FILE = os.path.join(DATA_DIR, 'api_key.json')

# Load API key
def load_api_key():
    if not os.path.exists(API_KEY_FILE):
        print("Error: Gemini API key file not found.")
        return None
    with open(API_KEY_FILE, 'r') as file:
        keys = json.load(file)
    return keys.get("gemini_api_key")

# Generic Gemini API call function
def query_gemini(prompt_text):
    api_key = load_api_key()
    if not api_key:
        return "Error: Gemini API key is missing. Run installer first."

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt_text}
                ]
            }
        ]
    }

    try:
        response = requests.post(f"{url}?key={api_key}", headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"API Error {response.status_code}: {response.text}"

    except Exception as e:
        return f"Request failed: {e}"
