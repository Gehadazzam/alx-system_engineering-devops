#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit"""


import requests as rq


def top_ten(subreddit):
    """If not a valid subreddit, print None"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Custom"}
    response = rq.get(url, headers=headers)

    if response.status_code != 200:
        print(None)
    else:
        for post in response.json()["data"]["children"]:
            print(post["data"]["title"])
