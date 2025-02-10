#!/usr/bin/python3
"""
Script that fetches an employee's TODO list progress using a REST API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{url}/users/{user_id}").json()
    todos = requests.get(f"{url}/todos", params={"userId": user_id}).json()

    if not user:
        sys.exit(1)

    employee_name = user.get("name")
    done_tasks = [task.get("title") for task in todos if task.get("completed")]
    total_tasks = len(todos)

    print(f"Employee {employee_name} is done with tasks"
          f"({len(done_tasks)}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task}")
