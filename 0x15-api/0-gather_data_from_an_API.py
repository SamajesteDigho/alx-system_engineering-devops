#!/usr/bin/python3
"""
    Here the code description and module
"""
import requests
import sys


args = sys.argv
if __name__ == "__main__":
    if len(args) > 0:
        id = args[1]
        url1 = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        url2 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        try:
            response1 = requests.get(url=url1)
            user = response1.json()
            response2 = requests.get(url=url2)
            todos = response2.json()

            completed = []
            for x in todos:
                if x['completed'] is True:
                    completed.append(x)

            print("Employee {} is done with tasks({}/{}):".
                  format(user['name'], len(completed), len(todos)))
            for x in completed:
                print("\t{}".format(x['title']))
        except Exception as e:
            pass
