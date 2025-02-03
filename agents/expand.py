import os
import requests
from utils.base_agent import BaseAgent

class ExpandAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.endpoint = "http://localhost:11434/api/generate"

    def process(self, message, code="", readme=""):
        # Convert message to string if it's a dict
        message_str = message if isinstance(message, str) else str(message)
        
        data = {
            "model": self.model,
            "prompt": f"""{message_str} Analyze the following content and extract the following values from the following keys: 
            Psychological Profile Extraction (Keys and Value Descriptions)
	1.	Emotional Tone – Analyzed sentiment of the text (positive, neutral, negative). (String: “Positive”, “Neutral”, “Negative”)
	2.	Dominant Emotion – Primary emotion conveyed (joy, anger, sadness, etc.). (String: “Joy”, “Anger”, “Sadness”, etc.)
	3.	Cognitive Complexity – Measures depth of thought and abstraction. (Number: Scale of 1-10, where 1 is simple and 10 is highly complex)
	4.	Openness to Experience – Determines level of curiosity and exploration. (Number: Scale of 1-10)
	5.	Conscientiousness – Assesses organization and discipline in the text. (Number: Scale of 1-10)
	6.	Extraversion – Measures social engagement or withdrawal. (Number: Scale of 1-10)
	7.	Agreeableness – Evaluates friendliness and cooperativeness. (Number: Scale of 1-10)
	8.	Neuroticism – Measures emotional stability. (Number: Scale of 1-10)
	9.	Confidence Level – Extracts indicators of certainty vs. doubt. (Number: Scale of 1-10)
	10.	Formality of Writing – Measures casual vs. structured writing. (Number: Scale of 1-10, where 1 is informal and 10 is highly formal)
	11.	Self-Reference Frequency – Counts first-person pronouns (I, me, my). (Number: Percentage of self-references per total words)
	12.	Use of Technical Jargon – Measures complexity of vocabulary. (Number: Percentage of technical terms per total words)
	13.	Hedging Language – Identifies uncertainty (e.g., “might,” “perhaps”). (Number: Percentage of hedging words per total words)
	14.	Persuasive Language – Detects argumentation strategies. (Number: Scale of 1-10, where 1 is neutral and 10 is highly persuasive)
	15.	Optimism vs. Pessimism – Determines future outlook in statements. (String: “Optimistic”, “Neutral”, “Pessimistic”)
	16.	Problem-Solving Orientation – Identifies structured problem resolution attempts. (Number: Scale of 1-10)
	17.	Ambiguity vs. Specificity – Measures how precise the language is. (Number: Scale of 1-10)
	18.	Use of Metaphors & Analogies – Detects abstract explanatory patterns. (Number: Percentage of metaphors per total words)
	19.	Intensity of Emotion – Measures emotional expressiveness. (Number: Scale of 1-10)
	20.	Frequency of Humor or Sarcasm – Identifies humorous intent. (Number: Scale of 1-10)
	21.	Use of Imperatives – Detects commands or direct instructions. (Number: Percentage of imperative sentences per total words)
	22.	Introspective vs. External Focus – Identifies whether the user talks about personal experience or external topics. (String: “Introspective”, “Balanced”, “External”)
	23.	Risk Aversion – Evaluates cautious vs. risk-taking tendencies. (Number: Scale of 1-10)
	24.	Resilience Language – Detects expressions of perseverance and adaptability. (Number: Scale of 1-10)
	25.	Use of Collective Language – Measures group affiliation (“we,” “us”). (Number: Percentage of collective pronouns per total words)

Programming Idea Extraction (Keys and Value Descriptions)
	26.	Main Programming Topic – Extracts the primary area of discussion. (String: “Web Development”, “Machine Learning”, “Databases”, etc.)
	27.	Programming Language Mentioned – Identifies the programming languages in use. (List of strings: [“Python”, “JavaScript”, etc.])
	28.	Frameworks and Libraries Mentioned – Extracts names of technologies used. (List of strings: [“React”, “Django”, etc.])
	29.	Problem Statement – Extracts the core technical issue being discussed. (String: Brief problem description)
	30.	Proposed Solution Complexity – Evaluates depth of proposed solutions. (Number: Scale of 1-10)
	31.	Use of Design Patterns – Identifies named software patterns. (List of strings: [“Singleton”, “Factory”, etc.])
	32.	Algorithmic Complexity Discussion – Measures technical depth of algorithm talk. (Number: Scale of 1-10)
	33.	Performance Optimization Concerns – Detects efficiency discussions. (Number: Scale of 1-10)
	34.	Security Considerations – Extracts references to security best practices. (Number: Scale of 1-10)
	35.	Scalability Discussion – Identifies concerns about large-scale applications. (Number: Scale of 1-10)
	36.	Code Readability Consideration – Extracts whether clarity is a focus. (Number: Scale of 1-10)
	37.	Testing and Debugging Approaches – Identifies methodologies used. (List of strings: [“Unit Tests”, “Debugging”, “CI/CD”])
	38.	Tooling and Environment Mentions – Extracts references to IDEs, linters, etc. (List of strings: [“VS Code”, “Docker”, etc.])
	39.	Dependency Management Discussion – Identifies package management strategies. (List of strings: [“pip”, “npm”, etc.])
	40.	Database Discussion – Extracts database-related topics. (String: “SQL”, “NoSQL”, “Graph Databases”)
	41.	Data Structure Mentions – Identifies key structures being discussed. (List of strings: [“Array”, “HashMap”, etc.])
	42.	Concurrency and Parallelism Concerns – Detects threading or async talk. (Number: Scale of 1-10)
	43.	API Design Discussion – Evaluates REST, GraphQL, or microservices mentions. (String: “REST”, “GraphQL”, “Microservices”)
	44.	Error Handling Strategies – Extracts how errors are managed. (List of strings: [“Try-Catch”, “Logging”, etc.])
	45.	Automated Deployment Mention – Identifies CI/CD pipeline discussions. (String: “Jenkins”, “GitHub Actions”, etc.)
	46.	UI/UX Considerations – Detects front-end usability discussions. (Number: Scale of 1-10)
	47.	Code Reusability Mentions – Extracts whether modularity is discussed. (Number: Scale of 1-10)
	48.	Project Management Methodologies – Identifies Agile, Scrum, etc. (List of strings: [“Agile”, “Scrum”, “Kanban”])
	49.	Collaboration and Open Source Involvement – Detects teamwork discussions. (Number: Scale of 1-10)
	50.	Ethical Considerations in Programming – Identifies discussions about responsible AI, privacy, etc. (Number: Scale of 1-10)""",
            "stream": False
        }
        
        try:
            response = requests.post(self.endpoint, json=data).json()
            design_spec = response.get('response', '')
            enhanced_message = f"{message_str}\n\n{design_spec}"
            
            return {
                'message': enhanced_message,

            }
        except Exception as e:
            print(f"Error in ExpandAgent: {str(e)}")
            return {
                'message': message_str,

            }
