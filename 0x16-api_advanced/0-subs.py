#!/usr/bin/python3
"""
    Here is the exo 0
"""
import requests


def number_of_subscribers(subreddit):
    """ Get the number of subscribers in a subreddit """
    headers = {
        # "Authorization": "bearer {}".format(bearer),
        "user-agent": "ALX_SE_Project/0.1 by SamajesteDigho"
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    return data.get("subscribers", 0)
