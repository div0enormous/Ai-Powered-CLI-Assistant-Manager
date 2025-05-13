import os
import sys
import argparse
import subprocess
from .config import Config
from .gemini_integration import GeminiAPI
from .error_handler import ErrorHandler
from .terminal_setup import TerminalSetup
from .utils.logger import setup_logger

logger = setup_logger()

class CLIManager:
    def __init__(self):
        """Initialize the CLI Manager with configuration and components"""
        self.config = Config()
        self.gemini = GeminiAPI(self.config)
        self.error_handler = ErrorHandler(self.gemini)
        self.terminal_setup = TerminalSetup(self.config)
        
    def run(self, args):
        """Main entry point for CLI Manager"""
        parser = self.create_parser()
        parsed_args = parser.parse_args(args)
        
        # Handle initialization for shell integration
        if parsed_args.init:
            print(self.terminal_setup.get_init_script())
            return
            
        # Handle settings commands
        if parsed_args.command == "settings":
            return self.handle_settings(parsed_args)
            
        # Handle explanation requests
        if parsed_args.command == "explain":
            return self.handle_explain(parsed_args.query)
            
        # Handle last error explanation
        if parsed_args.command == "last-error":
            return self.error_handler.explain_last_error()
            
        # Show help if no command specified
        if not parsed_args.command:
            parser.print_help()
            
    def create_parser(self):
        """Create command line argument parser"""
        parser = argparse.ArgumentParser(
            description=f"{self.config.get('name', 'CLI Manager')} - AI-powered terminal assistant"
        )
        
        # Global arguments
        parser.add_argument('--init', action='store_true', help='Output shell initialization script')
        parser.add_argument('--version', action='store_true', help='Show version information')
        
        # Subcommands
        subparsers = parser.add_subparsers(dest='command')
        
        # Settings command
        settings_parser = subparsers.add_parser('settings', help='Manage CLI Manager settings')
        settings_parser.add_argument('--list', action='store_true', help='List all settings')
        settings_parser.add_argument('--set', nargs=2, metavar=('KEY', 'VALUE'), help='Set a setting')
        settings_parser.add_argument('--reset', action='store_true', help='Reset settings to defaults')
        settings_parser.add_argument('--font', help='Set the font')
        settings_parser.add_argument('--text-size', help='Set the text size')
        settings_parser.add_argument('--color', help='Set the color theme')
        settings_parser.add_argument('--name', help='Set the assistant name')
        settings_parser.add_argument('--word-limit', type=int, help='Set word limit for responses')
        
        # Explain command
        explain_parser = subparsers.add_parser('explain', help='Explain a command or error')
        explain_parser.add_argument('query', nargs='*', help='The command or error to explain')
        
        # Last-error command
        subparsers.add_parser('last-error', help='Explain the last error that occurred')
        
        return parser
        
    def handle_settings(self, args):
        """Handle settings subcommand"""
        if args.list:
            settings = self.config.get_all()
            print(f"\n{self.config.get('name', 'CLI Manager')} Settings:")
            print("=" * 40)
            for key, value in settings.items():
                print(f"{key}: {value}")
            print("=" * 40)
            return
            
        if args.reset:
            self.config.reset_to_defaults()
            print("Settings reset to defaults.")
            return
            
        # Handle individual setting changes
        if args.set:
            key, value = args.set
            self.config.set(key, value)
            print(f"Setting '{key}' updated to '{value}'")
            return
            
        # Handle specialized settings
        if args.font:
            self.config.set("font", args.font)
            print(f"Font updated to '{args.font}'")
            
        if args.text_size:
            self.config.set("text_size", args.text_size)
            print(f"Text size updated to '{args.text_size}'")
            
        if args.color:
            self.config.set("color_theme", args.color)
            print(f"Color theme updated to '{args.color}'")
            
        if args.name:
            self.config.set("name", args.name)
            print(f"Assistant name updated to '{args.name}'")
            
        if args.word_limit:
            self.config.set("word_limit", args.word_limit)
            print(f"Word limit updated to {args.word_limit}")
    
    def handle_explain(self, query):
        """Handle explanation requests using Gemini API"""
        if not query:
            print("Please provide a query to explain.")
            return
            
        query_text = " ".join(query)
        result = self.gemini.explain(query_text)
        print(result)
        
def main():
    """Entry point for the CLI Manager"""
    manager = CLIManager()
    manager.run(sys.argv[1:])

if __name__ == "__main__":
    main()
