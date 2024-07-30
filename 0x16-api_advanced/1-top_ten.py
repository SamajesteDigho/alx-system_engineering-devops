#!/usr/bin/python3
"""
    Here is the exo 1
"""
import requests


def top_ten(subreddit):
    """ Get the number of subscribers in a subreddit """
    headers = {"user-agent": "request"}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return None

    data = response.json().get("data", {}).get('children', [])
    top_10_posts = '\n'.join(
        [post.get('data', {}).get('title') for post in data])
    print(top_10_posts)
