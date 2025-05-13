import os
import google.generativeai as genai
from .utils.logger import setup_logger
from .utils.text_formatter import format_text

logger = setup_logger()

class GeminiAPI:
    """Integration with Google's Gemini API for AI-powered explanations"""
    
    def __init__(self, config):
        """Initialize the Gemini API client"""
        self.config = config
        self.setup_client()
        
    def setup_client(self):
        """Set up the Gemini API client with API key"""
        api_key = self.config.api_key
        if not api_key:
            logger.warning("No Gemini API key found. Set GEMINI_API_KEY environment variable or update config.")
            return
            
        try:
            self.client = genai.Client(api_key=api_key)
            logger.info("Gemini API client initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Gemini API client: {e}")
            self.client = None
            
    def explain(self, query, context=None):
        """Get explanation from Gemini API for a query"""
        if not self.client:
            return "Error: Gemini API client not initialized. Check API key."
            
        model_name = self.config.get("gemini_model", "gemini-2.0-flash")
        word_limit = self.config.get("word_limit", 150)
        
        prompt = self._build_prompt(query, context, word_limit)
        
        try:
            response = self.client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            
            if response.text:
                return format_text(response.text, self.config)
            else:
                return "No explanation available."
                
        except Exception as e:
            logger.error(f"Error in Gemini API request: {e}")
            return f"Error: Failed to get explanation from Gemini API ({str(e)})"
            
    def explain_error(self, error_message, command=None):
        """Get explanation for a specific error message"""
        context = f"Command: {command}\n" if command else ""
        context += f"Error: {error_message}"
        return self.explain("Explain this error and how to fix it", context)
        
    def _build_prompt(self, query, context=None, word_limit=150):
        """Build a prompt for the Gemini API"""
        prompt = f"""
        You are a helpful terminal assistant that provides concise, clear explanations for terminal commands and errors.
        
        Please explain the following in a clear, concise way (max {word_limit} words):
        
        Query: {query}
        """
        
        if context:
            prompt += f"\nContext:\n{context}"
            
        prompt += f"\nProvide a practical solution or explanation with examples if helpful."
        
        return prompt
