#!/bin/bash

echo "=========================================================="
echo "          Uninstalling CLI-Manager - Terminal Helper       "
echo "=========================================================="

# Detect shell
SHELL_NAME=$(basename "$SHELL")
echo "Detected shell: $SHELL_NAME"

SHELL_RC=""
case "$SHELL_NAME" in
    "bash")
        SHELL_RC=~/.bashrc
        ;;
    "zsh")
        SHELL_RC=~/.zshrc
        ;;
    "fish")
        SHELL_RC=~/.config/fish/config.fish
        ;;
    *)
        echo "Unsupported shell: $SHELL_NAME. You'll need to manually remove CLI Manager from your shell startup."
        ;;
esac

# Remove from shell startup file
if [ -n "$SHELL_RC" ] && [ -f "$SHELL_RC" ]; then
    echo "Removing CLI Manager from $SHELL_RC..."
    sed -i '/# CLI Manager initialization/d' "$SHELL_RC"
    sed -i '/eval "$(cli-manager --init)"/d' "$SHELL_RC"
fi

# Remove CLI Manager executable
if [ -f ~/.local/bin/cli-manager ]; then
    echo "Removing CLI Manager executable..."
    rm ~/.local/bin/cli-manager
fi

# Remove virtual environment if it exists
if [ -d ~/.cli-manager-env ]; then
    echo "Removing CLI Manager virtual environment..."
    rm -rf ~/.cli-manager-env
fi

# Remove configuration
echo "Removing CLI Manager configuration..."
rm -rf ~/.cli-manager

echo "=========================================================="
echo "Uninstallation complete!"
echo "You may need to restart your terminal for changes to take effect."
echo "=========================================================="
