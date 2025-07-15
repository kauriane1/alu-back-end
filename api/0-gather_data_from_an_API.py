#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Check for correct usage
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch user info
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        sys.exit(1)

    employee_name = user_response.json().get('name')

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos if task.get('completed')]

    # Output
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(todos)}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
