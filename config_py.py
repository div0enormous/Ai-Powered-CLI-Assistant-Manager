import os
import yaml
from pathlib import Path

class Config:
    """Configuration management for CLI Manager"""
    
    def __init__(self):
        """Initialize the configuration manager"""
        self.config_dir = os.path.expanduser("~/.cli-manager/config")
        self.config_file = os.path.join(self.config_dir, "config.yaml")
        self.defaults = {
            "name": "CLI Manager",
            "font": "default",
            "text_size": "medium",
            "color_theme": "default",
            "word_limit": 150,
            "api_key": os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE"),
            "gemini_model": "gemini-2.0-flash",
            "shell_history_file": self._get_default_history_file(),
            "aliases": {
                "cm": "cli-manager"
            }
        }
        self._ensure_config_exists()
        self.settings = self._load_config()
        
    def _get_default_history_file(self):
        """Get the default shell history file path"""
        shell = os.environ.get("SHELL", "").split("/")[-1]
        if shell == "bash":
            return os.path.expanduser("~/.bash_history")
        elif shell == "zsh":
            return os.path.expanduser("~/.zsh_history")
        elif shell == "fish":
            return os.path.expanduser("~/.local/share/fish/fish_history")
        else:
            return os.path.expanduser("~/.bash_history")  # Default fallback
            
    def _ensure_config_exists(self):
        """Ensure the configuration directory and file exist"""
        os.makedirs(self.config_dir, exist_ok=True)
        
        if not os.path.exists(self.config_file):
            self._save_config(self.defaults)
            
    def _load_config(self):
        """Load the configuration from file"""
        try:
            with open(self.config_file, 'r') as f:
                config = yaml.safe_load(f)
                
            # Update with any missing defaults
            for key, value in self.defaults.items():
                if key not in config:
                    config[key] = value
                    
            return config
        except Exception as e:
            print(f"Error loading config: {e}")
            return self.defaults.copy()
            
    def _save_config(self, config):
        """Save the configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                yaml.dump(config, f, default_flow_style=False)
        except Exception as e:
            print(f"Error saving config: {e}")
            
    def get(self, key, default=None):
        """Get a configuration value"""
        return self.settings.get(key, default)
        
    def set(self, key, value):
        """Set a configuration value"""
        self.settings[key] = value
        self._save_config(self.settings)
        
    def get_all(self):
        """Get all configuration values"""
        return self.settings.copy()
        
    def reset_to_defaults(self):
        """Reset configuration to defaults"""
        self.settings = self.defaults.copy()
        self._save_config(self.settings)
        
    @property
    def api_key(self):
        """Get the API key with environment variable priority"""
        env_key = os.environ.get("GEMINI_API_KEY")
        if env_key:
            return env_key
        return self.settings.get("api_key", self.defaults["api_key"])
