import os
import requests
from utils.base_agent import BaseAgent

class AnalyzeAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.endpoint = "http://localhost:11434/api/generate"

    def process(self, message, code="", readme=""):
        # Convert message to string if it's a dict
        message_str = message if isinstance(message, str) else str(message)
        
        data = {
            "model": self.model,
            "prompt": f"""({message_str}) You will receive structured Reddit content analysis data based on two main categories: **Psychological Profile Extraction** and **Programming Metrics Extraction**. Your task is to analyze the provided data according to the outlined metrics and generate two distinct markdown-formatted outputs:

1. **A Psychological Profile Report** – A detailed written analysis in markdown format describing the psychological characteristics of the Reddit user based on extracted metrics.

2. **A Programming Project Outline** – A structured markdown document detailing the technical discussion, extracted programming ideas, and an architecture overview of a potential project inspired by the extracted insights.

**Input Structure:**

  

The structured input data will contain two sections:

  

**1. Psychological Profile Extraction**

  

For each metric, the data will contain either a categorical label (e.g., "Positive", "Joy"), a numerical scale (1-10), or a percentage-based metric. These values should be used to construct a meaningful psychological analysis. The key attributes include:

• **Emotional Tone** (Positive, Neutral, Negative)

• **Dominant Emotion** (Joy, Anger, Sadness, etc.)

• **Cognitive Complexity** (1-10)

• **Openness to Experience** (1-10)

• **Conscientiousness** (1-10)

• **Extraversion** (1-10)

• **Agreeableness** (1-10)

• **Neuroticism** (1-10)

• **Confidence Level** (1-10)

• **Formality of Writing** (1-10)

• **Self-Reference Frequency** (Percentage)

• **Use of Technical Jargon** (Percentage)

• **Hedging Language** (Percentage)

• **Persuasive Language** (1-10)

• **Optimism vs. Pessimism** (Optimistic, Neutral, Pessimistic)

• **Problem-Solving Orientation** (1-10)

• **Ambiguity vs. Specificity** (1-10)

• **Use of Metaphors & Analogies** (Percentage)

• **Intensity of Emotion** (1-10)

• **Frequency of Humor or Sarcasm** (1-10)

• **Use of Imperatives** (Percentage)

• **Introspective vs. External Focus** (Introspective, Balanced, External)

• **Risk Aversion** (1-10)

• **Resilience Language** (1-10)

• **Use of Collective Language** (Percentage)

  

**2. Programming Metrics Extraction**

  

This section will contain structured data extracted from the programming-related discussion. Your task is to use these extracted elements to construct a markdown-formatted programming guide that outlines the technical topic, programming challenges, and a structured plan for a potential application. The extracted metrics include:

• **Main Programming Topic** (Web Development, Machine Learning, etc.)

• **Programming Language Mentioned** (List: Python, JavaScript, etc.)

• **Frameworks and Libraries Mentioned** (List: React, Django, etc.)

• **Problem Statement** (Brief description)

• **Proposed Solution Complexity** (1-10)

• **Use of Design Patterns** (List: Singleton, Factory, etc.)

• **Algorithmic Complexity Discussion** (1-10)

• **Performance Optimization Concerns** (1-10)

• **Security Considerations** (1-10)

• **Scalability Discussion** (1-10)

• **Code Readability Consideration** (1-10)

• **Testing and Debugging Approaches** (List: Unit Tests, Debugging, CI/CD)

• **Tooling and Environment Mentions** (List: VS Code, Docker, etc.)

• **Dependency Management Discussion** (List: pip, npm, etc.)

• **Database Discussion** (SQL, NoSQL, Graph Databases)

• **Data Structure Mentions** (List: Array, HashMap, etc.)

• **Concurrency and Parallelism Concerns** (1-10)

• **API Design Discussion** (REST, GraphQL, Microservices)

• **Error Handling Strategies** (List: Try-Catch, Logging, etc.)

• **Automated Deployment Mention** (Jenkins, GitHub Actions, etc.)

• **UI/UX Considerations** (1-10)

• **Code Reusability Mentions** (1-10)

• **Project Management Methodologies** (List: Agile, Scrum, Kanban)

• **Collaboration and Open Source Involvement** (1-10)

• **Ethical Considerations in Programming** (1-10)

**Expected Output Format:**

  

**1. Markdown-Formatted Psychological Profile Analysis**

  

Using the structured psychological metrics, generate a **detailed written analysis** in markdown format. This analysis should explain the psychological characteristics inferred from the data, provide insights into the author’s personality, and discuss key trends in their writing.

  

**2. Markdown-Formatted Programming Guide and Project Architecture**

  

Using the extracted programming metrics, generate a **structured markdown document** that contains:

• A high-level summary of the technical discussion.

• An identified **problem statement** based on the extracted programming concerns.

• A detailed **architecture overview** of a new project that could be developed based on the discussed ideas.

• Relevant **frameworks, libraries, and best practices** to be used.

• Considerations regarding **performance, security, scalability, and testing**.

**Guidelines for Generating the Output:**

• Ensure the **Psychological Profile Analysis** reads as a natural, well-structured assessment, using the extracted numerical and categorical data to describe key traits.

• The **Programming Guide** should be formatted with clear sections (e.g., Problem Statement, Proposed Solution, Architecture, Tools, Best Practices).

• Use appropriate **markdown formatting** with headings (#), subheadings (##), lists (-), and code blocks where necessary.

• The generated text should be structured as **a blog post** suitable for publication.""",
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
            print(f"Error in AnalyzeAgent: {str(e)}")
            return {
                'message': message_str,

            }
