#!/usr/bin/python3
""" queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit
the function should return None."""


import requests as rq


def recurse(subreddit, hot_list=[], counter=None):
    """If not a valid subreddit, return None."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    parmeters = {"after": counter}
    response = rq.get(url, headers=headers, params=parmeters)

    if response.status_code != 200:
        return None

    else:
        for post in response.json()["data"]["children"]:
            hot_list.append(post["data"]["title"])
            counter = response.json()["data"]["after"]
            if counter is not None:
                recurse(subreddit, hot_list, counter)
            else:
                return hot_list
