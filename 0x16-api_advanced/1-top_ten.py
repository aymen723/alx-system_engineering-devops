#!/usr/bin/python3
"""fetch the hot postes."""
import requests


def top_ten(subreddit):
    """fetch the title of 10 hotest posts."""
    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    h = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    p = {
        "limit": 10
    }
    res = requests.get(link, headers=h, params=p,
                            allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    results = res.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
