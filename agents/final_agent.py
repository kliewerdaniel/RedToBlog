import os
import requests
import json
from utils.base_agent import BaseAgent

class FinalAgent(BaseAgent):
    def __init__(self, model="default-model"):
        super().__init__()
        self.endpoint = "http://localhost:11434/api/generate"
        self.model = model

    def process(self, prompt):
        message = prompt.get('message', '')
        message_str = message if isinstance(message, str) else json.dumps(message, indent=2)
        
        data = {
            "model": self.model,
            "prompt": f"""Using these metrics ({message_str}) generate a final report that combines the psychological profile and programming project outline into a single markdown document. The report should provide a comprehensive analysis of the Reddit user's psychological characteristics and propose a technical project inspired by the extracted programming ideas. The report should be well-structured, detailed, and insightful, combining both psychological and technical aspects into a coherent narrative.""",
            "stream": False,
        }


        response = requests.post(self.endpoint, json=data)
       
        json_response = response.json()  # Parse JSON response
            
            # Get the result from the response
        result = json_response.get('response', 'No response from API')
        enhanced_message = f"{message_str}\n\n{result}"
        return {
            'message': enhanced_message,

            }

