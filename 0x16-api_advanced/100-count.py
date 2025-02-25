#!/usr/bin/python3
"""Module to count given keywords in the titles of articles on a subreddit"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """Recursively queries the Reddit API"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "custom_user_agent"
    }
    params = {
        "after": after,
        "limit": 100
    }

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            word_lower = word.lower()
            word_count[word_lower] = word_count.get(word_lower, 0) + \
                title.count(word_lower)

    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, word_count, after)

    sorted_words = sorted(
        [(k, v) for k, v in word_count.items() if v > 0],
        key=lambda x: (-x[1], x[0])
    )

    for word, count in sorted_words:
        print("{}: {}".format(word, count))
