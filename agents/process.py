import os
import re
from datetime import datetime
import requests
import json
from utils.base_agent import BaseAgent


class ProcessAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.endpoint = "http://localhost:11434/api/generate"

    def _extract_json(self, text):
        # Find JSON-like structure between curly braces
        pattern = r'\{(?:[^{}]|(?R))*\}'
        matches = re.findall(pattern, text, re.DOTALL)
        
        if not matches:
            return None
        
        # Try each match until we find valid JSON
        for match in matches:
            try:
                # Parse to validate and return first valid JSON
                parsed = json.loads(match)
                return match
            except json.JSONDecodeError:
                continue
        return None

    def process(self, message, code="", readme=""):
        # Ensure `message` is a string
        message_str = message if isinstance(message, str) else str(message)

        # Prepare the payload
        data = {
            "model": self.model,
            "prompt": f"""Using this analysis: ({message_str})""",
            "stream": False
        }

            # Make the API request
        response = requests.post(self.endpoint, json=data)
        json_response = response.json()

        json_result = self._extract_json(json_response)
        if json_result:
          return json_result
          
          
        # Return the original message if an error occurs
        return {'message': message_str}





