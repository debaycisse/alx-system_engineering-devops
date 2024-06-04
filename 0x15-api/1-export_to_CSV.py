#!/usr/bin/python3
"""This module defines a script that takes a used ID to generate a
list todos of a user, both the completed and uncompleted todos"""
import json
import requests
import sys


def store_user_todos(userId, username, data_list, f_path):
    """stores a given user's todo in a given csv file

    Args:
        userId - the id of the given user
        username - the username of the given user
        data_list - the list of tasks of a given user
        f_path - path to the csv file
    """
    for task_obj in data_list:
        with open(f_path, "a") as f:
            data = '"{}","{}","{}","{}"\n'\
                .format(userId, username,
                        task_obj.get('completed'), task_obj.get('title'))
            f.write(data)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} user_id")
    else:
        todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
            .format(sys.argv[1])
        user_url = 'https://jsonplaceholder.typicode.com/users?id={}'\
            .format(sys.argv[1])
        todo_res = json.loads(requests.get(todo_url).text)
        emp_name_res = json.loads(requests.get(user_url).text)
        emp_username = emp_name_res[0].get('username')
        file_path = "{}.csv".format(sys.argv[1])
        store_user_todos(sys.argv[1], emp_username, todo_res, file_path)
