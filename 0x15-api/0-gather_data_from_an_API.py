#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
using a given employee ID and a REST API.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)

    if response.status_code == 200:
        employee_data = response.json()
        name = employee_data.get("name", "")
    else:
        print("Failed to fetch employee data")
        sys.exit(1)

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(url)

    if todos_response.status_code == 200:
        todos = todos_response.json()
        done_tasks = [todo for todo in todos if todo.get("completed")]
        tasks = len(todos)
        count_done = len(done_tasks)

        print(f"Employee {name} is done with tasks({count_done}/{tasks}):")
        print(f"\t {name}: {count_done}")
        print(f"\t TOTAL: {tasks}")
        for task in done_tasks:
            print(f"\t {task['title'].lstrip()}")
    else:
        print("Failed to fetch employee's TODO list")
