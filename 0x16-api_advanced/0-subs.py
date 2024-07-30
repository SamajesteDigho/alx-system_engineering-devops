#!/usr/bin/python3
"""
    Here is the exo 0
"""
import requests


def number_of_subscribers(subreddit):
    """ Get the number of subscribers in a subreddit """
    headers = {'User-Agent': 'request'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url=url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get('data', {})
    number = data.get('subscribers', 0)
    return number
