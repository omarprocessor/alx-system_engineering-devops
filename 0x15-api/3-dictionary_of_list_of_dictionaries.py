"""This script fetches user tasks from an API
and exports them to a JSON file."""

import json
import requests


def fetch_and_export_tasks():
    """Fetch tasks from API and export them to a JSON file."""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    tasks_dict = {}

    for user in users:
        user_id = str(user["id"])
        username = user["username"]

        tasks_dict[user_id] = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in todos
            if task["userId"] == user["id"]
        ]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks_dict, json_file)


if __name__ == "__main__":
    fetch_and_export_tasks()
