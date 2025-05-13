# CLI MANAGER
> 🖥️ Your AI-Powered Linux Terminal Companion

<div align="center">

![CLI MANAGER Logo](https://img.shields.io/badge/CLI-MANAGER-blue?style=for-the-badge&logo=linux&logoColor=white)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Gemini API](https://img.shields.io/badge/Powered%20by-Google%20Gemini-brightgreen)](https://gemini.google.com/)

</div>

## 🚀 Overview

**CLI MANAGER** enhances your Linux terminal experience with AI-powered assistance. It helps troubleshoot errors, correct command syntax, explain command usage, and personalize your CLI environment—all powered by the Google Gemini API.

Install once, and CLI MANAGER integrates seamlessly with your system, providing an intelligent, always-ready assistant for your terminal tasks.

<div align="center">
  <img src="/api/placeholder/700/350" alt="CLI MANAGER Demo" />
</div>

## ✨ Features

- **🔍 AI-Powered Error Explanation**  
  Get clear, understandable explanations for terminal errors.

- **🛠️ Smart Fix Suggestions**  
  Receive intelligent fixes tailored to your specific errors.

- **✏️ Syntax Correction**  
  Detect and correct mistyped commands automatically.

- **📚 Command Usage Explanations**  
  Understand how common Linux commands and their flags work.

- **📜 Error & Command History**  
  Access your last 5 logged errors for reference.

- **🎨 Customizable Appearance**  
  Personalize your CLI Manager's name, text color, and font size.

- **🔄 One-Time Setup & Auto-Start**  
  Install once and CLI MANAGER will be ready in every terminal session.

## 📋 Installation

### Prerequisites

- Python 3.8+
- Linux-based operating system
- Google Gemini API key

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/cli_manager.git
cd cli_manager
```

### Step 2: Run the Installer

```bash
cd system
bash installer.sh
```

This will:
- Install required dependencies
- Prompt you to enter your Google Gemini API key
- Configure initial settings
- Optionally set up auto-start for CLI MANAGER on terminal launch

## 🖱️ Usage

Once installed, CLI MANAGER is available via simple terminal commands:

### Examples

```bash
# Get an explanation for an error
cli explain "Permission denied"

# Get fix suggestions for a failed command
cli fix "ls -l /root"

# Learn how to use a command
cli usage "chmod"

# View or modify settings
settings -list
```

### Settings Menu

To customize appearance and preferences:

```bash
settings -list
```

Options include:
- Change CLI tool name
- Change text color
- Change font size
- Reset to default settings

## 🔑 API Key Setup

During installation, you'll be asked to provide your Google Gemini API key, which will be securely stored locally on your system.

If you need to update it later:

```bash
nano data/api_key.json
```

## 📁 Directory Structure

```
CLI_MANAGER/
├── cli_manager.py               # Main CLI program
├── modules/
│   ├── __init__.py
│   ├── error_explainer.py
│   ├── fix_suggester.py
│   ├── syntax_corrector.py
│   ├── command_explainer.py
│   ├── history_manager.py
│   └── settings_manager.py
│
├── api/
│   └── ai_api.py
│
├── data/
│   ├── api_key.json
│   ├── settings.json
│   └── error_logs.json
│
├── system/
│   ├── installer.sh
│   └── autostart.sh
│
├── LICENSE
├── README.md
├── requirements.txt
├── .gitignore
└── cli_manager.service
```

## 📦 Dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Powered by Google Gemini API
- Inspired by the needs of Linux power users everywhere

---

<div align="center">
  <p>Crafted with ❤️ for Linux power users</p>
</div>
