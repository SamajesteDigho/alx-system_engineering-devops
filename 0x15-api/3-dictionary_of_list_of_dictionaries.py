#!/usr/bin/python3
"""
    Here the code description and module
"""
import json
import requests


def parse_format_data(user, todos):
    list_td = []
    for x in todos:
        dict_td = {}
        dict_td["task"] = "{}".format(x['title'])
        dict_td["completed"] = x['completed']
        dict_td["username"] = "{}".format(user['username'])
        list_td.append(dict_td)
    return list_td


if __name__ == "__main__":
    url1 = "https://jsonplaceholder.typicode.com/users".format(id)
    url2 = "https://jsonplaceholder.typicode.com/users/{}/todos"
    try:
        data = {}
        response1 = requests.get(url=url1)
        users = response1.json()

        for user in users:
            tdu = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                user["id"])
            response2 = requests.get(url=tdu)
            todos = response2.json()

            completed = []
            for x in todos:
                if x['completed'] is True:
                    completed.append(x)

            print("Employee {} is done with tasks({}/{}):".
                  format(user['name'], len(completed), len(todos)))
            for x in completed:
                print("\t {}".format(x['title']))

            data["{}".format(user['id'])] = parse_format_data(user, todos)

        with open('todo_all_employees.json', 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(e)
