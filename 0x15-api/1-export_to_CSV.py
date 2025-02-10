#!/usr/bin/python3
"""
Script that fetches an employee's TODO list and exports it to a CSV file.
"""

import csv
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
    filename = f"{user_id}.csv"

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username, task.get("completed"),
                             task.get("title")])
