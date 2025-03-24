from storage import task_exists

def validate_add_task(tasks, task_name, start_date, end_date):
    status, msg = True, "Task added successfully!"
    # Check if data is empty
    if not task_name:
        status, msg = False, "Task name cannot be empty!"
    elif not start_date:
        status, msg = False, "Start date cannot be empty!"
    elif not end_date:
        status, msg = False, "End date cannot be empty!"
    # Check if start date is before end date
    elif start_date > end_date:
        status, msg = False, "Start date cannot be after end date!"
    # Check if task already exists
    elif task_exists(tasks, task_name):
        status, msg = False, "Task already exists! Pick another name."
    return status, msg

def sort_tasks(tasks):
    imcomplete_tasks = [task for task in tasks if task["status"] == "incomplete"]
    complete_tasks = [task for task in tasks if task["status"] == "complete"]

    imcomplete_tasks.sort(key=lambda x: x["deadline"])

    return imcomplete_tasks + complete_tasks