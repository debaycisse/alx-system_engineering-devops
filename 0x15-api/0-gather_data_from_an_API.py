#!/usr/bin/python3
"""This module defines a script that takes a used ID to generate a
list todos of a user, both the completed and uncompleted todos"""
from requests import get
from sys import argv
import json


def count_task(data_list, key, value):
    """counts a number of key where value is equal to a given value
    in a given data (dictionary)

    Args:
        data - the dictionary whose data is checked
        key - the key whose value is compared
        value - the value to compare to

    Return:
        number of objects whose keys' values match up
    """
    count = 0
    for obj in data_list:
        if obj.get(key) == value:
            count += 1
    return count


def display_completed_tasks(data_list, task_status):
    """display a list of completed tasks from in given list of task objects

    Args:
        data - the dictionary whose data is checked
        task_status - the status of tasks to be printed
    """
    for task in data_list:
        if task.get('completed') == task_status:
            print("\t {}".format(task.get('title')))


if __name__ == '__main__':

    if len(argv) < 2:
        print(f"Usage: python3 {argv[0]} user_id")
    else:
        todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
            .format(argv[1])
        user_url = 'https://jsonplaceholder.typicode.com/users?id={}'\
            .format(argv[1])
        todo_res = json.loads(get(todo_url).text)
        emp_name_res = json.loads(get(user_url).text)
        done_tasks = count_task(todo_res, 'completed', True)
        total_tasks = count_task(todo_res, 'completed', False) + done_tasks
        print(f"Employee {emp_name_res[0].get('name')}",
              f"is done with tasks {done_tasks}/{total_tasks}")
        display_completed_tasks(todo_res, True)
