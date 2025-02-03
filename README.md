# Reddit Data Analysis

This project is designed to fetch and analyze data from Reddit. It uses various agents to process the data and generate insights.


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/kliewerdaniel/RedditDataAnalysis.git
    cd RedditDataAnalysis
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Configure the environment variables in the [.env](http://_vscodecontentref_/3) file.

Included is a .sampledotenv for an empty version you can fill in with these instructions:

To interact with Reddit’s API, you’ll need to create an application within your Reddit account.


Navigate to https://www.reddit.com/prefs/apps.
Create a New Application:
Click on “Create App” or “Create Another App”.
Fill out the form:

About URL: (Leave blank or provide a relevant URL)
Redirect URI: http://localhost:8080 (Required but not used for scripts)

Click “Create App”.

Retrieve Credentials:

Client ID: Displayed under the app name.

Client Secret: Displayed alongside the Client ID.

User Agent: A descriptive string, e.g., python:RedditBlogGenerator:1.0 (by /u/yourusername)


2. Run the main script:
    ```sh
    python main.py
    ```

## Project Components

- **agents/**: Contains the different agents used for data analysis.
  - `analyze.py`: Script for analyzing the fetched data.
  - `expand.py`: Script for expanding the data.
  - `final_agent.py`: The final agent script that combines all functionalities.

- **utils/**: Utility scripts.
  - `base_agent.py`: Base class for agents.
  - `config.py`: Configuration settings.
  - `reddit_fetch.py`: Script for fetching data from Reddit.

- **venv/**: Virtual environment directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.