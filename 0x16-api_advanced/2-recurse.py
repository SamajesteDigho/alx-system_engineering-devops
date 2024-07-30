#!/usr/bin/python3
"""
    Here is the exo 2
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Get the number of subscribers in a subreddit """
    headers = {
        # "Authorization": "bearer {}".format(bearer),
        "user-agent": "request"
    }
    params = {"limit" : 100}
    
    url = "https://www.reddit.com/r/{}/hot".format(subreddit)
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    children = data.get('children', [])
    for child in children:
        hot_list.append(child.get('title'))

    after = data.get('after')
    if after:
        recurse(subreddit, hot_list=hot_list, after=after)
    else:
        return hot_list
