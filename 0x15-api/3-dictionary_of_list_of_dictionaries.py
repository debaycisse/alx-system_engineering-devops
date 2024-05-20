#!/usr/bin/python3
"""This module defines a script that takes a used ID to generate a
list todos of a user, both the completed and uncompleted todos"""
import json
import requests


def store_all_todos(data_list, users_list, f_path):
    """stores all users' todos in to a given json file

    Args:
        data_list - the list of all todos
        users_list - a list of all users
        f_path - path to the given json file
    """
    obj = {}
    # loop through each user and collect each user's todos
    for user_obj in users_list:
        # create an object to collect a user's todos, using user's id as a key
        inner_obj = {"{}".format(user_obj.get('id')): []}
        # fill up the user's todo inside the empty list, created above
        for todo_obj in data_list:
            if todo_obj.get('userId') == user_obj.get('id'):
                inner_obj["{}".format(user_obj.get('id'))].append(
                    {"username": user_obj.get('username'),
                     "task": todo_obj.get('title'),
                     "completed": todo_obj.get('completed')}
                )
        obj.update(inner_obj)

    with open(f_path, "w") as f:
        json.dump(obj, f)


if __name__ == '__main__':

    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_list = json.loads(requests.get(todos_url).text)
    users_list = json.loads(requests.get(users_url).text)
    file_path = "todo_all_employees.json"
    store_all_todos(todos_list, users_list, file_path)
