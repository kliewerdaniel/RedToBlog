
import praw
import os
from dotenv import load_dotenv

# Configure logging


load_dotenv()

class RedditMonitor:
    def __init__(self):
        try:
            self.reddit = praw.Reddit(
                client_id=os.getenv("REDDIT_CLIENT_ID"),
                client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                user_agent=os.getenv("REDDIT_USER_AGENT"),
                username=os.getenv("REDDIT_USERNAME"),
                password=os.getenv("REDDIT_PASSWORD")
            )
            user = self.reddit.user.me()
            if user is None:
                raise ValueError("Authentication failed. Check your Reddit credentials.")
            self.username = user.name
            print(f"Authenticated as: {self.username}")
        except Exception as e:
            print(f"Error during Reddit authentication: {e}")
            self.username = None

    def fetch_recent_posts(self, limit=10):
        if not self.username:
            print("Cannot fetch posts: User is not authenticated.")
            return []
        user = self.reddit.redditor(self.username)
        posts = []
        try:
            for submission in user.submissions.new(limit=limit):
                posts.append({
                    "type": "post",
                    "title": submission.title,
                    "selftext": submission.selftext,
                    "created_utc": submission.created_utc,
                    "url": submission.url
                })
        except Exception as e:
            print(f"Error fetching posts: {e}")
        return posts

    def fetch_recent_comments(self, limit=10):
        if not self.username:
            print("Cannot fetch comments: User is not authenticated.")
            return []
        user = self.reddit.redditor(self.username)
        comments = []
        try:
            for comment in user.comments.new(limit=limit):
                comments.append({
                    "type": "comment",
                    "body": comment.body,
                    "created_utc": comment.created_utc,
                    "link_id": comment.link_id
                })
        except Exception as e:
            print(f"Error fetching comments: {e}")
        return comments

    def fetch_all_recent_activity(self, limit=20):
        posts = self.fetch_recent_posts(limit)
        comments = self.fetch_recent_comments(limit)
        total = posts + comments
        return total
