#!/usr/bin/python3
"""a func to fetch all host postes in reddit for a subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """fetch a list of postes for subreddit."""
    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    h = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    p = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(link, headers=h, params=p,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    res = response.json().get("data")
    after = res.get("after")
    count += res.get("dist")
    for c in res.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
