#!/usr/bin/env python3

import csv
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]

    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)

    response_user = requests.get(url_user)
    response_todos = requests.get(url_todos)

    if response_user.status_code != 200:
        print('User not found')
        exit(1)

    if response_todos.status_code != 200:
        print('Todos not found')
        exit(1)

    user_data = response_user.json()
    todos_data = response_todos.json()

    user_id = user_data['id']
    username = user_data['username']
    filename = "{}.csv".format(user_id)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos_data:
            task_completed = "True" if todo['completed'] else "False"
            task_title = todo['title']
            writer.writerow([user_id, username, task_completed, task_title])

    print("Tasks for user {} exported to {}".format(username, filename))
