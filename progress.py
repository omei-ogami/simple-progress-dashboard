import datetime

def get_bar_color(days_left):
    if days_left <= 3:
        return "red"
    elif days_left <= 7:
        return "orange"
    else:
        return "green"
    
# day left
def get_days_left(task_data):
    deadline = datetime.datetime.strptime(task_data['deadline'], '%Y-%m-%d')
    daysLeft = (deadline - datetime.datetime.today()).days + 1
    return daysLeft
    
# Progress Bar Chart
def progress_bar_chart(task_data):
    daysLeft = get_days_left(task_data)

    if task_data['duration'] == 0:
        width = 100
    else:
        width = 100 - (daysLeft/task_data['duration']) * 100

    if task_data['status'] == 'complete':
        color = "green"
        width = 100
    else:
        color = get_bar_color(daysLeft)

    progress_html = f"""
        <div style="width: 100%; height: 10px; background-color: #eee; border-radius: 5px;">
            <div style="width: {width}%; height: 10px; background-color: {color}; border-radius: 5px;"></div>
        </div>
    """
        
    return progress_html