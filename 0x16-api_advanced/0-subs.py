#!/usr/bin/python3
"""a function to sub a specifque subreddit."""
import requests


def number_of_subscribers(subreddit):
    """fetch nbr of subs in a subreddit."""
    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    h = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    res = requests.get(link, headers=h, allow_redirects=False)
    if res.status_code == 404:
        return 0
    results = res.json().get("data")
    return results.get("subscribers")
