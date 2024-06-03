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
            url2 = url2.format(user["id"])
            response2 = requests.get(url=url2)
            todos = response2.json()
            data["{}".format(user['id'])] = parse_format_data(user, todos)

        with open('todo_all_employees.json', 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(e)
