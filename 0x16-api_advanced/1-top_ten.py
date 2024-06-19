#!/usr/bin/python3
"""
    Here is the exo 1
"""
import requests


def top_ten(subreddit):
    """ Get the number of subscribers in a subreddit """
    bearer = "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzE4ODQxOTA2LjA2Mjc3MSwiaWF0IjoxNzE4NzU1NTA2LjA2Mjc3MSwianRpIjoiT3dkd2NWY0kwWm1pY0xzaE5ZM0FOOEI4NzdwWE9BIiwiY2lkIjoiSmVZamhQeFlXMGNxUlBmaHJNLWhQdyIsImxpZCI6InQyXzEycnFqdDZ2OHQiLCJhaWQiOiJ0Ml8xMnJxanQ2djh0IiwibGNhIjoxNzE4NzQ3NjE4MzczLCJzY3AiOiJlSnlLVnRKU2lnVUVBQURfX3dOekFTYyIsImZsbyI6OX0.eGO23wQGQB0h8vK8AQQZbiysFMiHVETp3E6rmXG6uxmid3DOibNGRnwlhL9Kii25qVMRUurvgKWcoQjLeLNpQcFU8vuAIkBvZgYUxpjbzUtn6wKYPcNyQT2KzunzC81ArrC8BzX3FF7KLg3Ra__N4LTUbp5-MrT2kFBtOfjkE8AEMn0qlTOmjX0yV2MZP2JpfV5KBaNnkZvzvx7mb3OlrU5Z4afFavtC8wMTSP_H_VlUQfU41KWyFThvMO2U-X7nbU7SQDQoetNsJRsRFzRoVVSG2ZuyOHw5OZ4vu8kpxhuGrrpER0peh9lq8kgjYtvqN1mwIVDXR1j5Nl3qylL_SQ"
    headers = {
        "Authorization": "bearer {}".format(bearer),
        "User-Agent": "ALX_SE_Project/0.1 by SamajesteDigho"
    }
    url = "https://oauth.reddit.com/r/{}/hot?limit=10".format(subreddit)
    response = requests.get(url, headers=headers)
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
