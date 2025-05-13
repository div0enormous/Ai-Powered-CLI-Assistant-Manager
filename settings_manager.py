import json
import os

# Constants
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
SETTINGS_FILE = os.path.join(DATA_DIR, 'settings.json')

# Load settings
def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {
            "cli_name": "CLI_MANAGER",
            "text_color": "default",
            "font_style": "normal",
            "text_size": "medium"
        }
    with open(SETTINGS_FILE, 'r') as file:
        return json.load(file)

# Save settings
def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as file:
        json.dump(settings, file, indent=4)

# List current settings
def list_settings():
    settings = load_settings()
    print("\n[ Current CLI Settings ]\n")
    for key, value in settings.items():
        print(f"{key}: {value}")

# Update a specific setting
def update_setting(key, value):
    settings = load_settings()
    if key not in settings:
        print(f"Invalid setting: {key}")
        return
    settings[key] = value
    save_settings(settings)
    print(f"{key} updated to {value}.")
