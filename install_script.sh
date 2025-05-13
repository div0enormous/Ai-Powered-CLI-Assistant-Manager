#!/bin/bash

echo "=========================================================="
echo "          Installing CLI-Manager - Terminal Helper         "
echo "=========================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed. Please install Python 3 and try again."
    exit 1
fi

# Create virtual environment if possible
echo "Setting up Python environment..."
python3 -m pip install --user virtualenv &> /dev/null
if command -v virtualenv &> /dev/null; then
    python3 -m virtualenv ~/.cli-manager-env &> /dev/null
    source ~/.cli-manager-env/bin/activate
    ENV_PATH=~/.cli-manager-env
    echo "Using virtual environment at $ENV_PATH"
else
    echo "Virtualenv not available, installing in user space..."
    ENV_PATH="user space"
fi

# Install Python dependencies
echo "Installing dependencies..."
python3 -m pip install -r requirements.txt

# Create config directory
mkdir -p ~/.cli-manager/config

# Copy default config
cp config/default_config.yaml ~/.cli-manager/config/config.yaml

# Install the CLI Manager
echo "Installing CLI Manager..."
python3 -m pip install -e .

# Add to shell startup based on shell type
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
        echo "Unsupported shell: $SHELL_NAME. You'll need to manually add CLI Manager to your shell startup."
        echo "Add the following to your shell startup file:"
        echo "eval \"\$(cli-manager --init)\""
        ;;
esac

if [ -n "$SHELL_RC" ]; then
    # Check if already in RC file
    if grep -q "cli-manager --init" "$SHELL_RC"; then
        echo "CLI Manager already added to $SHELL_RC"
    else
        echo "" >> "$SHELL_RC"
        echo "# CLI Manager initialization" >> "$SHELL_RC"
        echo "eval \"\$(cli-manager --init)\"" >> "$SHELL_RC"
        echo "Added CLI Manager to $SHELL_RC"
    fi
fi

# Create CLI Manager command
mkdir -p ~/.local/bin
cat > ~/.local/bin/cli-manager << 'EOF'
#!/bin/bash

# Find the CLI Manager Python script
if [ -d ~/.cli-manager-env ]; then
    source ~/.cli-manager-env/bin/activate
fi

python3 -m cli_manager "$@"
EOF

chmod +x ~/.local/bin/cli-manager

# Create alias in ~/.cli-manager/config
echo "alias cm='cli-manager'" >> ~/.cli-manager/config/aliases

echo "=========================================================="
echo "Installation complete!"
echo "To start using CLI Manager, either:"
echo "  1. Restart your terminal"
echo "  2. Run: source $SHELL_RC"
echo ""
echo "CLI Manager commands:"
echo "  cli-manager --help      : Show help"
echo "  cli-manager settings    : Configure settings"
echo "  cm                      : Quick command alias"
echo "=========================================================="
