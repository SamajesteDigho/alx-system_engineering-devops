#!/usr/bin/python3
"""
    Here is the exo 2
"""
import requests


def recurse_merge(subreddit, hot_list=[], count=0, after=None):
    """ Get the number of subscribers in a subreddit """
    headers = {
        # "Authorization": "bearer {}".format(bearer),
        "User-Agent": "ALX_SE_Project/0.1 by SamajesteDigho"
    }
    if after is None:
        url = "https://www.reddit.com/r/{}/hot?limit=99&count={}".format(subreddit, count)
    else:
        url = "https://www.reddit.com/r/{}/hot?limit=99&count={}&after{}".format(
            subreddit, count, after)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        try:
            children = data['data']['children']
            after = data['data']['after']
            count += int(data['data']['dist'])
            for child in children:
                hot_list.append(child['data']['title'])
            if after is not None:
                recurse_merge(subreddit, hot_list=hot_list, count=count, after=after)
        except Exception:
            return hot_list
    return hot_list


def recurse(subreddit, hot_list=[]):
    """ Recursively """
    return recurse_merge(subreddit, hot_list)
