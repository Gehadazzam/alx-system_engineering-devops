#!/usr/bin/python3
""" queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit
the function should return None."""


import requests as rq

def recurse(subreddit, hot_list=[]):
    """If not a valid subreddit, return None."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = rq.get(url, headers=headers)

    if response.status_code != 200:
        return None
