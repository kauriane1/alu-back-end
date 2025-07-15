#!/usr/bin/python3
"""
This script uses a REST API to fetch and display the TODO list progress
of a given employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]

    # Get employee info
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    user_res = requests.get(user_url).json()
    emp_name = user_res.get("name")

    # Get todos for employee
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    todos = requests.get(todo_url).json()

    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)

    print(f"Employee {emp_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
