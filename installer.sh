#!/bin/bash

# CLI MANAGER INSTALLER
# One-time setup script for CLI MANAGER

clear
echo "=========================================="
echo "        CLI MANAGER INSTALLATION          "
echo "=========================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Error: Python 3 is not installed. Install Python 3 and retry."
    exit 1
fi

# Install required Python packages
echo "[+] Installing required Python packages..."
pip3 install -r ../requirements.txt

# Create data directory if it doesn't exist
if [ ! -d "../data" ]; then
    mkdir ../data
fi

# Create default settings.json if not exists
if [ ! -f "../data/settings.json" ]; then
    cat > ../data/settings.json <<EOL
{
    "cli_name": "CLI MANAGER",
    "text_color": "green",
    "font_size": "medium"
}
EOL
fi

# Create empty error_logs.json if not exists
if [ ! -f "../data/error_logs.json" ]; then
    echo "[]" > ../data/error_logs.json
fi

# Prompt for Gemini API Key
echo ""
read -p "Enter your Google Gemini API key: " GEMINI_API_KEY

# Save API key to api_key.json
echo "[+] Saving API key..."
cat > ../data/api_key.json <<EOL
{
    "gemini_api_key": "$GEMINI_API_KEY"
}
EOL

# Offer to setup autostart
echo ""
read -p "Do you want to auto-start CLI MANAGER in every terminal session? (y/n): " autostart_choice

if [ "$autostart_choice" = "y" ]; then
    bash ./autostart.sh
fi

echo ""
echo "[✓] Installation Complete!"
echo "You can now use 'cli' and 'settings -list' commands."
echo "=========================================="
