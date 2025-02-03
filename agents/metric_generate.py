import os
import re
from datetime import datetime
import requests
import json
from utils.base_agent import BaseAgent


class MetricAgent(BaseAgent):

    def __init__(self):
        super().__init__()
        self.endpoint = "http://localhost:11434/api/generate"

    def process(self, message, code="", readme=""):
        # Ensure `message` is a string
        message_str = message if isinstance(message, str) else str(message)

        # Prepare the payload
        data = {
            "model": self.model,
            "prompt": f"""Using this analysis: {message_str} Analyze the previous content and create a JSON object that contains the following structured data:

{{
  "psychological_profile": {{
    "emotional_tone": {{
      "description": "Analyzed sentiment of the text.",
      "type": "string",
      "values": ["Positive", "Neutral", "Negative"]
    }},
    "dominant_emotion": {{
      "description": "Primary emotion conveyed in the text.",
      "type": "string",
      "values": ["Joy", "Anger", "Sadness", "Fear", "Surprise", "Disgust", "Neutral"]
    }},
    "cognitive_complexity": {{
      "description": "Measures depth of thought and abstraction in the writing.",
      "type": "integer",
      "range": [1, 10]
    }},
    "openness_to_experience": {{
      "description": "Determines the level of curiosity, creativity, and intellectual engagement.",
      "type": "integer",
      "range": [1, 10]
    }},
    "conscientiousness": {{
      "description": "Assesses organization, discipline, and thoroughness in writing.",
      "type": "integer",
      "range": [1, 10]
    }},
    "extraversion": {{
      "description": "Measures social engagement, enthusiasm, and talkativeness.",
      "type": "integer",
      "range": [1, 10]
    }},
    "agreeableness": {{
      "description": "Evaluates friendliness, cooperativeness, and empathy.",
      "type": "integer",
      "range": [1, 10]
    }},
    "neuroticism": {{
      "description": "Measures emotional stability and tendency toward negative emotions.",
      "type": "integer",
      "range": [1, 10]
    }},
    "confidence_level": {{
      "description": "Indicates certainty vs. doubt in statements.",
      "type": "integer",
      "range": [1, 10]
    }},
    "formality_of_writing": {{
      "description": "Measures the degree of structured and professional tone.",
      "type": "integer",
      "range": [1, 10]
    }},
    "self_reference_frequency": {{
      "description": "Percentage of words that are self-referential (e.g., 'I', 'me', 'my').",
      "type": "float",
      "unit": "percentage"
    }},
    "use_of_technical_jargon": {{
      "description": "Percentage of words that are domain-specific technical terms.",
      "type": "float",
      "unit": "percentage"
    }},
    "hedging_language": {{
      "description": "Percentage of words or phrases that indicate uncertainty (e.g., 'might', 'perhaps').",
      "type": "float",
      "unit": "percentage"
    }},
    "persuasive_language": {{
      "description": "Measures the use of rhetorical devices and argumentation strategies.",
      "type": "integer",
      "range": [1, 10]
    }},
    "optimism_vs_pessimism": {{
      "description": "Determines the outlook on future events.",
      "type": "string",
      "values": ["Optimistic", "Neutral", "Pessimistic"]
    }},
    "problem_solving_orientation": {{
      "description": "Identifies structured attempts to resolve issues.",
      "type": "integer",
      "range": [1, 10]
    }},
    "ambiguity_vs_specificity": {{
      "description": "Measures precision and clarity of language.",
      "type": "integer",
      "range": [1, 10]
    }},
    "use_of_metaphors_analogies": {{
      "description": "Percentage of words that are metaphors or analogies.",
      "type": "float",
      "unit": "percentage"
    }},
    "intensity_of_emotion": {{
      "description": "Measures the expressiveness and strength of emotions conveyed.",
      "type": "integer",
      "range": [1, 10]
    }},
    "frequency_of_humor_or_sarcasm": {{
      "description": "Measures humor or sarcasm usage.",
      "type": "integer",
      "range": [1, 10]
    }},
    "use_of_imperatives": {{
      "description": "Percentage of sentences that contain commands or directives.",
      "type": "float",
      "unit": "percentage"
    }},
    "introspective_vs_external_focus": {{
      "description": "Classifies whether the writing is focused on personal experience or external topics.",
      "type": "string",
      "values": ["Introspective", "Balanced", "External"]
    }},
    "risk_aversion": {{
      "description": "Measures cautious vs. risk-taking tendencies.",
      "type": "integer",
      "range": [1, 10]
    }},
    "resilience_language": {{
      "description": "Detects expressions of perseverance and adaptability.",
      "type": "integer",
      "range": [1, 10]
    }},
    "use_of_collective_language": {{
      "description": "Percentage of words indicating group affiliation (e.g., 'we', 'us').",
      "type": "float",
      "unit": "percentage"
    }}
  }},
  "programming_metrics": {{
    "main_programming_topic": {{
      "description": "Primary area of discussion in programming content.",
      "type": "string"
    }},
    "programming_languages_mentioned": {{
      "description": "List of programming languages referenced.",
      "type": "array",
      "items": "string"
    }},
    "frameworks_and_libraries_mentioned": {{
      "description": "List of frameworks and libraries referenced.",
      "type": "array",
      "items": "string"
    }},
    "problem_statement": {{
      "description": "Brief description of the technical issue being discussed.",
      "type": "string"
    }},
    "proposed_solution_complexity": {{
      "description": "Evaluates depth of proposed solutions.",
      "type": "integer",
      "range": [1, 10]
    }},
    "use_of_design_patterns": {{
      "description": "List of software design patterns mentioned.",
      "type": "array",
      "items": "string"
    }},
    "algorithmic_complexity_discussion": {{
      "description": "Measures depth of algorithm-related discussion.",
      "type": "integer",
      "range": [1, 10]
    }},
    "performance_optimization_concerns": {{
      "description": "Evaluates concerns about code performance.",
      "type": "integer",
      "range": [1, 10]
    }},
    "security_considerations": {{
      "description": "Evaluates references to security best practices.",
      "type": "integer",
      "range": [1, 10]
    }},
    "scalability_discussion": {{
      "description": "Measures discussion on handling large-scale applications.",
      "type": "integer",
      "range": [1, 10]
    }},
    "code_readability_consideration": {{
      "description": "Evaluates emphasis on clean and readable code.",
      "type": "integer",
      "range": [1, 10]
    }},
    "testing_and_debugging_approaches": {{
      "description": "List of mentioned testing and debugging techniques.",
      "type": "array",
      "items": "string"
    }},
    "tooling_and_environment_mentions": {{
      "description": "List of development tools and environments mentioned.",
      "type": "array",
      "items": "string"
    }},
    "dependency_management_discussion": {{
      "description": "List of dependency/package management tools mentioned.",
      "type": "array",
      "items": "string"
    }},
    "database_discussion": {{
      "description": "Mentions of database technologies.",
      "type": "string"
    }},
    "error_handling_strategies": {{
      "description": "List of error-handling techniques discussed.",
      "type": "array",
      "items": "string"
    }},
    "ui_ux_considerations": {{
      "description": "Measures emphasis on user experience and interface design.",
      "type": "integer",
      "range": [1, 10]
    }},
    "ethical_considerations_in_programming": {{
      "description": "Evaluates discussions about ethical programming topics.",
      "type": "integer",
      "range": [1, 10]
    }}
  }}
}}

Return only the JSON object containing the psychological profile and programming metrics.
""",
            "stream": False
        }

        try:
            # Make the API request
            response = requests.post(self.endpoint, json=data)
            json_response = response.json()
            
            # Extract the response content
            design_spec = json_response.get('response', 'No response key in API result')
            enhanced_message = f"{message_str}\n\n{design_spec}"
            
            # Create simplified output with just the response
            output_data = {
                'response': design_spec
            }
            
            # Save just the response to a JSON file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"metric_output_{timestamp}.json"
            with open(filename, 'w') as json_file:
                json.dump(output_data, json_file, indent=4)
            
            return {
                'message': enhanced_message
            }
        except requests.exceptions.RequestException as req_err:
            print(f"Request error in MetricAgent: {str(req_err)}")
        except Exception as e:
            print(f"General error in MetricAgent: {str(e)}")
        
        # Return the original message if an error occurs
        return {
            'message': message_str
        }