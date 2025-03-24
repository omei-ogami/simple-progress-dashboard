import json
import streamlit as st
from progress import get_days_left


TASKS_FILE = "task.json"

# read json file
def read_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
            return tasks
    except (FileNotFoundError):
        print("Error: Could not read tasks file.")
        return []
    
# write json file
def write_tasks(task):
    with open(TASKS_FILE, "w") as f:
        json.dump(task, f, indent=4)
    st.rerun()

# check if task exists
def task_exists(tasks, task_name):
    return any(task["name"] == task_name for task in tasks)

# delete task
def delete_task(tasks, task_name):
    tasks = [task for task in tasks if task["name"]!= task_name]
    write_tasks(tasks)
    return tasks

# overedue
def check_overdue(tasks):
    for task in tasks:
        if get_days_left(task) < 0:
            delete_task(tasks, task["name"])