#!/usr/bin/python3
"""
    Here is the exo 0
"""
import requests
from os import getenv
from dotenv import load_dotenv
load_dotenv()


def number_of_subscribers(subreddit):
    """ Get the number of subscribers in a subreddit """
    headers = {
        "Authorization": "bearer {}".format(getenv('BEARER')),
        "User-Agent": "ALX_SE_Project/0.1 by SamajesteDigho"
    }
    url = "https://oauth.reddit.com/r/{}/about".format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data['data']['subscribers'])
        return data['data']['subscribers']
    return 0
