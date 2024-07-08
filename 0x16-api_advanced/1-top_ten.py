#!/usr/bin/python3
"""
    Here is the exo 1
"""
import requests


def top_ten(subreddit):
    """ Get the number of subscribers in a subreddit """
    headers = {
        # "Authorization": "bearer {}".format(bearer),
        "User-Agent": "ALX_SE_Project/0.1 by SamajesteDigho"
    }
    url = "https://www.reddit.com/r/{}/hot?limit=10".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        try:
            children = data['data']['children']
            for child in children:
                print(child['data']['title'])
        except Exception as e:
            print(None)
    else:
        print(None)
