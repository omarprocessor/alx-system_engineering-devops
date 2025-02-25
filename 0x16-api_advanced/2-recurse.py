#!/usr/bin/python3
"""Module to recursively get all hot article titles of a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of all hot article titles of a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "custom_user_agent"}
    params = {"after": after, "limit": 100}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json().get("data", {})
        posts = data.get("children", [])
        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))

        after = data.get("after")
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list

    return None
