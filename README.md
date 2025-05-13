# CLI-Manager

A smart terminal companion that helps explain and solve terminal errors using Google's Gemini AI.

## Features

- **Automatic Error Detection**: Intercepts terminal errors and provides AI-powered explanations
- **AI-Powered Assistance**: Uses Google's Gemini 2.0 API to provide helpful explanations
- **One-Time Setup**: Install once and it's available for all terminal sessions
- **Customizable**: Change the name, colors, fonts, and more
- **Easy Installation**: Simple one-line installer

## Installation

```bash
git clone https://github.com/yourusername/cli-manager.git
cd cli-manager
bash install.sh
```

## Usage

After installation, CLI-Manager runs automatically in your terminal.

### Basic Commands

```bash
# Get help
cli-manager --help

# View and modify settings
cli-manager settings --list
cli-manager settings set name "My Assistant"
cli-manager settings set theme dark

# Use the shorthand alias
cm explain "How do I fix 'permission denied' errors?"
```

### Configuration Options

- **Name**: Change the assistant name (`--name`)
- **Font**: Customize terminal font (`--font`)
- **Text Size**: Adjust text size (`--text-size`)
- **Colors**: Set theme colors (`--colors`)
- **Word Limit**: Set response length (`--word-limit`)

## Examples

```bash
# Ask for help with a specific command
cm explain "What does chmod 755 do?"

# Change the text size
cli-manager settings set text-size large

# Set a word limit for responses
cli-manager settings set word-limit 100
```

## Uninstallation

```bash
cd cli-manager
bash uninstall.sh
```

## Requirements

- Python 3.8+
- Internet connection (for Gemini API)

## License

MIT License
