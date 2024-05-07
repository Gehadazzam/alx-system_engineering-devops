#!/usr/bin/python3
"""queries the Reddit API and returns
the number of subscribers
(not active users, total subscribers)
for a given subreddit."""


import requests as rq


def number_of_subscribers(subreddit):
    """If not a valid subreddit, return 0."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    response = rq.get(url, headers=headers)

    if response.status_code != 200:
        return 0
    else:
        return response.json()["data"]["subscribers"]
