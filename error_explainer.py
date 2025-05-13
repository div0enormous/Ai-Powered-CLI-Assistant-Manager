import json
import os
import requests

# Constants
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
API_KEY_FILE = os.path.join(DATA_DIR, 'api_key.json')

# Load Gemini API key
def load_api_key():
    with open(API_KEY_FILE, 'r') as file:
        keys = json.load(file)
    return keys.get("gemini_api_key")

API_KEY = load_api_key()

# Explain error function
def explain_error(error_message):
    print("[+] Explaining your error...")

    if not API_KEY:
        print("Error: Gemini API key not found. Run installer first.")
        return

    # Gemini API call setup
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"You are an expert Linux system admin. Explain this Linux terminal error message in simple terms: {error_message}"
                    }
                ]
            }
        ]
    }

    response = requests.post(f"{url}?key={API_KEY}", headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        try:
            explanation = result['candidates'][0]['content']['parts'][0]['text']
            print("\nExplanation:\n")
            print(explanation)
        except (KeyError, IndexError):
            print("Error: Unexpected API response format.")
    else:
        print(f"Error: API request failed — Status Code {response.status_code}")
        print(response.text)
