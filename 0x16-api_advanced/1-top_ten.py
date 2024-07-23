#!/usr/bin/python3
"""
    Here is the exo 1
"""
import requests


def top_ten(subreddit):
    """ Get the number of subscribers in a subreddit """
    headers = {
        # "Authorization": "bearer {}".format(bearer),
        "user-agent": "ALX_SE_Project/0.1 by SamajesteDigho"
    }
    url = "https://www.reddit.com/r/{}/hot?limit=10".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
    else:
        data = response.json().get("data", {})
        children = data.get('children', [])
        for child in children:
            print(child.get('data', {}).get('title'))
