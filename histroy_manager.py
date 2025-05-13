import json
import os
from datetime import datetime

# Constants
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
LOG_FILE = os.path.join(DATA_DIR, 'error_logs.json')

# Load log data
def load_logs():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, 'r') as file:
        return json.load(file)

# Save log data
def save_logs(logs):
    with open(LOG_FILE, 'w') as file:
        json.dump(logs, file, indent=4)

# Add a new error log
def add_error_log(error_text):
    logs = load_logs()
    new_log = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "error": error_text
    }
    logs.append(new_log)
    if len(logs) > 5:
        logs = logs[-5:]  # Keep only last 5
    save_logs(logs)

# Display logs
def view_error_logs():
    logs = load_logs()
    if not logs:
        print("No errors logged yet.")
        return

    print("\n[Last 5 Error Logs]:\n")
    for log in logs:
        print(f"[{log['timestamp']}] {log['error']}")
