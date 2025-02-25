#!/usr/bin/python3
"""Module to get the top 10 hot posts of a given subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "custom_user_agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print(None)
