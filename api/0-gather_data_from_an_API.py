#!/usr/bin/python3
"""This module defines a script that connects to an API."""
import sys
import requests


def fetch_employee_todo_progress(employee_id):
    """
    Fetches information about the employee's TODO 
    list progress using a REST API.

    Args:
    employee_id (int): The ID of the employee 
    whose TODO list progress is to be fetched.

    Returns:
    None: The function prints the progress 
    information to the standard output.

    Example:
    fetch_employee_todo_progress(1)
    # Output:
    # Employee Leanne Graham is done with tasks 
    (5/20):
    #     delectus aut autem
    #     quis ut nam facilis et officia qui
    #     fugiat veniam minus
    #     et porro tempora
    #     laboriosam mollitia et enim quasi 
          adipisci quia provident illum
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Failed to fetch user information.")
        return

    user_data = user_response.json()
    employee_name = user_data["name"]

    # Fetch todo list
    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print("Failed to fetch todo list.")
        return

    todo_data = todo_response.json()
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if 
                       task["completed"]]
    num_completed_tasks = len(completed_tasks)

    # Print progress
    print(f"Employee {employee_name} is done with tasks 
          ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        fetch_employee_todo_progress(employee_id)