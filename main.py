import os
import requests
import json
from datetime import datetime
import networkx as nx
from dotenv import load_dotenv
from utils.base_agent import BaseAgent
from agents.final_agent import FinalAgent
from agents.analyze import AnalyzeAgent
from agents.expand import ExpandAgent
from utils.reddit_fetch import RedditMonitor
from agents.metric_generate import MetricAgent

def write_to_file(prompt, filename='output.txt'):
    with open(filename, 'a') as f:
        f.write("=== Iteration Output ===\n")
        f.write("Message:\n")
        f.write(prompt.get('message', '') + "\n\n")



def main():
    load_dotenv()

    # Initialize Reddit monitor
    reddit_monitor = RedditMonitor()
    if not reddit_monitor.username:
        logging.error("Reddit authentication failed. Exiting application.")
        return

    reddit_content = reddit_monitor.fetch_all_recent_activity(limit=4)
    print(f"Fetched {len(reddit_content)} recent posts and comments.")

    # Initialize agents
    agents = {
        'Expand': ExpandAgent(),
        'Analyze': AnalyzeAgent(),
        'Metric': MetricAgent(),
        'Final': FinalAgent()
    }

    # Create a directed graph to model the flow of data between agents
    G = nx.DiGraph()

    # Add nodes
    G.add_nodes_from(agents.keys())

    # Define edges to represent the flow between agents
    G.add_edges_from([
        ('Expand', 'Analyze'),
        ('Analyze', 'Metric'),
        ('Metric', 'Final'),
        ('Expand', 'Final'),
        ('Analyze', 'Final'),
        ('Metric', 'Final')
    ])

    # Initial prompt
    prompt = {'message': reddit_content}

    iteration = 0
    max_iterations = 1  # Safety limit to prevent infinite loops
    is_complete = False

    while iteration < max_iterations and not is_complete:
        iteration += 1
        print(f"--- Iteration {iteration} ---")

        # Process the prompt through the agents according to the graph
        for node in nx.topological_sort(G):
            if node != 'Final':
                agent = agents[node]
                try:
                    print(f"Processing with {node}Agent")
                    prompt = agent.process(prompt)
                    write_to_file(prompt)
                except Exception as e:
                    logging.error(f"An error occurred in {node}Agent: {e}")
                    return
            else:
                # Check completion with the FinalAgent
                is_complete = agents['Final'].process(prompt)
                print("Process is complete." if is_complete else "Continuing to next iteration.")

    if not is_complete:
        print("Reached maximum iterations without completion. Saving current progress.")

    # Save the final output
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"final_output_{timestamp}.txt"
    with open(filename, 'w') as f:
        f.write(f"Final Output ({timestamp}):\n\n")
        f.write("Message:\n")
        f.write(prompt.get('message', '') + "\n\n")

    print(f"Final progress has been saved to {filename}.")


if __name__ == "__main__":
    main()
