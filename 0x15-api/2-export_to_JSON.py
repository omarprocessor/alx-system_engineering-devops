#!/usr/bin/python3
"""
Script that fetches an employee's TODO list and exports it to a JSON file.
"""

import json
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

    username = user.get("username")
    filename = f"{user_id}.json"

    tasks = [{"task": task.get("title"), "completed": task.get("completed"),
              "username": username} for task in todos]

    with open(filename, "w") as file:
        json.dump({user_id: tasks}, file)
