import os
import re
import subprocess
from .utils.logger import setup_logger

logger = setup_logger()

class ErrorHandler:
    """Handle and explain terminal errors"""
    
    def __init__(self, gemini_api):
        """Initialize the error handler"""
        self.gemini = gemini_api
        
    def explain_last_error(self):
        """Explain the most recent error from shell history"""
        # Get last command that resulted in an error
        last_error = self._find_last_error()
        if not last_error:
            print("No recent errors found.")
            return
            
        command, error = last_error
        print(f"Last error command: {command}")
        print(f"Error message: {error}")
        print("\nExplanation:")
        explanation = self.gemini.explain_error(error, command)
        print(explanation)
        
    def _find_last_error(self):
        """Find the most recent command that resulted in an error"""
        try:
            # Try to get the last command with non-zero exit code
            result = subprocess.run(
                ["fc", "-ln", "-1"],
                capture_output=True, 
                text=True
            )
            last_command = result.stdout.strip()
            
            # Run the command again to get its error
            result = subprocess.run(
                last_command,
                shell=True,
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                return (last_command, result.stderr.strip())
                
            # If no error from last command, try to parse history
            return self._parse_history_for_error()
            
        except Exception as e:
            logger.error(f"Error finding last error: {e}")
            return self._parse_history_for_error()
            
    def _parse_history_for_error(self):
        """Parse shell history to find recent errors"""
        try:
            # Attempt to find errors in shell history
            history_file = os.environ.get("HISTFILE", os.path.expanduser("~/.bash_history"))
            
            if not os.path.exists(history_file):
                logger.error(f"History file not found: {history_file}")
                return None
                
            with open(history_file, 'r') as f:
                lines = f.readlines()
                
            # Start from the end and look for patterns that suggest errors
            for line in reversed(lines):
                line = line.strip()
                
                # Skip empty lines and common commands
                if not line or line.startswith("#") or line in ["ls", "cd", "pwd"]:
                    continue
                    
                # Test if this command results in an error
                result = subprocess.run(
                    line,
                    shell=True,
                    capture_output=True,
                    text=True
                )
                
                if result.returncode != 0:
                    return (line, result.stderr.strip())
                    
        except Exception as e:
            logger.error(f"Error parsing history: {e}")
            
        return None
        
    def intercept_errors(self, command, error):
        """Intercept and explain errors in real-time"""
        explanation = self.gemini.explain_error(error, command)
        return explanation
        
    def setup_trap(self):
        """Generate shell code to trap errors"""
        trap_code = """
        # CLI Manager error trap
        __cli_manager_error_handler() {
            local exit_code=$?
            if [ $exit_code -ne 0 ]; then
                local cmd=$(fc -ln -1)
                cli-manager --explain-error "$cmd" "$exit_code"
            fi
            return $exit_code
        }
        
        trap '__cli_manager_error_handler' ERR
        """
        return trap_code.strip()
