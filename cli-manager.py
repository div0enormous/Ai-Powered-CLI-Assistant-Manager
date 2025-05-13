#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CLI MANAGER - Main CLI program
A smart AI-powered Linux terminal companion
"""

import sys
import os
from modules import error_explainer, fix_suggester, syntax_corrector, command_explainer, history_manager, settings_manager

# Constants
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
API_KEY_FILE = os.path.join(DATA_DIR, 'api_key.json')
SETTINGS_FILE = os.path.join(DATA_DIR, 'settings.json')

# Load settings
def load_settings():
    import json
    with open(SETTINGS_FILE, 'r') as file:
        return json.load(file)

settings = load_settings()

# Print header with personalization
def print_header():
    name = settings.get("cli_name", "CLI MANAGER")
    color = settings.get("text_color", "green")

    color_codes = {
        "green": "\033[92m",
        "cyan": "\033[96m",
        "yellow": "\033[93m",
        "red": "\033[91m",
        "reset": "\033[0m"
    }
    color_code = color_codes.get(color, "\033[92m")

    print(f"{color_code}=== {name} ===\033[0m")

# CLI command dispatcher
def main():
    if len(sys.argv) < 2:
        print_header()
        print("Usage:")
        print("  cli explain [error_message]")
        print("  cli fix [command]")
        print("  cli syntax [command]")
        print("  cli usage [command]")
        print("  settings -list")
        sys.exit(1)

    command = sys.argv[1]

    if command == "explain":
        if len(sys.argv) < 3:
            print("Usage: cli explain [error_message]")
        else:
            error_message = " ".join(sys.argv[2:])
            error_explainer.explain_error(error_message)

    elif command == "fix":
        if len(sys.argv) < 3:
            print("Usage: cli fix [command]")
        else:
            command_text = " ".join(sys.argv[2:])
            fix_suggester.suggest_fix(command_text)

    elif command == "syntax":
        if len(sys.argv) < 3:
            print("Usage: cli syntax [command]")
        else:
            command_text = " ".join(sys.argv[2:])
            syntax_corrector.correct_command(command_text)

    elif command == "usage":
        if len(sys.argv) < 3:
            print("Usage: cli usage [command]")
        else:
            command_text = sys.argv[2]
            command_explainer.explain_command(command_text)

    elif command == "--settings" or (command == "settings" and len(sys.argv) > 2 and sys.argv[2] == "-list"):
        settings_manager.settings_menu()

    else:
        print("Invalid command. Run 'cli' for usage.")

if __name__ == "__main__":
    main()
