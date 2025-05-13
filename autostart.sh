#!/bin/bash

# CLI MANAGER AUTOSTART CONFIGURATION
# Adds autostart alias to ~/.bashrc or ~/.zshrc

echo "[+] Setting up CLI MANAGER autostart..."

# Determine user's shell config file
if [ -f "$HOME/.bashrc" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
elif [ -f "$HOME/.zshrc" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
else
    echo "Error: Could not find .bashrc or .zshrc file."
    exit 1
fi

# Add alias for CLI MANAGER if not already added
if ! grep -q "alias cli=" "$SHELL_CONFIG"; then
    echo "alias cli='python3 $(pwd)/../cli_manager.py'" >> "$SHELL_CONFIG"
    echo "alias settings='python3 $(pwd)/../cli_manager.py --settings'" >> "$SHELL_CONFIG"
    echo "[+] Aliases 'cli' and 'settings' added to $SHELL_CONFIG"
else
    echo "[!] Aliases already exist in $SHELL_CONFIG"
fi

# Source the config file to activate immediately
source "$SHELL_CONFIG"

echo "[✓] Autostart integration complete."
