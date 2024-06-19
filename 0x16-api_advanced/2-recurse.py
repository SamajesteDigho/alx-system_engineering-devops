#!/usr/bin/python3
"""
    Here is the exo 2
"""
import requests


def recurse_merge(subreddit, hot_list=[], count=0, after=None):
    """ Get the number of subscribers in a subreddit """
    bearer = "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzE4ODQxOTA2LjA2Mjc3MSwiaWF0IjoxNzE4NzU1NTA2LjA2Mjc3MSwianRpIjoiT3dkd2NWY0kwWm1pY0xzaE5ZM0FOOEI4NzdwWE9BIiwiY2lkIjoiSmVZamhQeFlXMGNxUlBmaHJNLWhQdyIsImxpZCI6InQyXzEycnFqdDZ2OHQiLCJhaWQiOiJ0Ml8xMnJxanQ2djh0IiwibGNhIjoxNzE4NzQ3NjE4MzczLCJzY3AiOiJlSnlLVnRKU2lnVUVBQURfX3dOekFTYyIsImZsbyI6OX0.eGO23wQGQB0h8vK8AQQZbiysFMiHVETp3E6rmXG6uxmid3DOibNGRnwlhL9Kii25qVMRUurvgKWcoQjLeLNpQcFU8vuAIkBvZgYUxpjbzUtn6wKYPcNyQT2KzunzC81ArrC8BzX3FF7KLg3Ra__N4LTUbp5-MrT2kFBtOfjkE8AEMn0qlTOmjX0yV2MZP2JpfV5KBaNnkZvzvx7mb3OlrU5Z4afFavtC8wMTSP_H_VlUQfU41KWyFThvMO2U-X7nbU7SQDQoetNsJRsRFzRoVVSG2ZuyOHw5OZ4vu8kpxhuGrrpER0peh9lq8kgjYtvqN1mwIVDXR1j5Nl3qylL_SQ"
    headers = {
        "Authorization": "bearer {}".format(bearer),
        "User-Agent": "ALX_SE_Project/0.1 by SamajesteDigho"
    }
    if after is None:
        url = "https://oauth.reddit.com/r/{}/hot?limit=99&count={}".format(subreddit, count)
    else:
        url = "https://oauth.reddit.com/r/{}/hot?limit=99&count={}&after{}".format(
            subreddit, count, after)
    response = requests.get(url, headers=headers)
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
