#!/usr/bin/python3
"""queries the Reddit API
parses the title of all hot articles
and prints a sorted count of given keywords"""


import requests as rq


def count_words(subreddit, words, counter=[], after=None):
    "Results should be printed in descending order, by the count"

    words = [w.lower() for w in words]

    if bool(counter) is False:
        for w in words:
            counter.append(0)

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = rq.get(url, headers=headers)

        if res.status_code != 200:
            return None

        else:
            for post in res.json()["data"]["children"]:
                for w in words:
                    if w in post["data"]["title"].lower():
                        counter[words.index(w)] += 1
            return counter

    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = rq.get(url, headers=headers)

        if res.status_code == 200:
            for post in res.json()["data"]["children"]:
                for w in words:
                    if w in post["data"]["title"].lower():
                        counter[words.index(w)] += 1
            after = res.json()["data"]["after"]
            if after:
                count_words(subreddit, words, counter, after)
            else:
                h = {}
                for key_word in list(set(words)):
                    i = words.index(key_word)
                    if counter[i] != 0:
                        h[words[i]] = counter[i] * words.count(words[i])

                for key, value in sorted(
                                    h.items(), key=lambda x: (-x[1], x[0])):
                    print("{}: {}".format(key, value))
