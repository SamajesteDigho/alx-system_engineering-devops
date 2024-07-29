#!/usr/bin/python3
"""
    Here is the exo 0
"""
import requests


def number_of_subscribers(subreddit):
    """ Get the number of subscribers in a subreddit """
    headers = {'user-agent': 'Mozilla/10.0/API'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get('data')
    number = data.get('subscribers')
    return number
