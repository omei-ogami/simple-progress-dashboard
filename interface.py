import streamlit as st
import datetime
from progress import progress_bar_chart, get_days_left
from utils import validate_add_task, sort_tasks
from storage import read_tasks, write_tasks, check_overdue, delete_task

# Initializing the session state
st.session_state.tasks = read_tasks()
check_overdue(st.session_state.tasks)
st.session_state.tasks = sort_tasks(st.session_state.tasks)

st.title("Progress Dashboard")

# Adding a new task
with st.container():
    st.header("Add a new task")
    task_name = st.text_input("Task name", key="task_name")
    start = st.date_input("Start date", datetime.date.today(), key="start")
    deadline = st.date_input("Deadline", datetime.date.today(), key="deadline")

    insertBtn, msg = st.columns([1, 5])
    with insertBtn:
        btn = st.button("Add task")
    with msg:
        if btn:
            succesful, msg = validate_add_task(st.session_state.tasks, task_name, start, deadline)
            if succesful:
                new_task = {
                    "name": task_name,
                    "start": str(start),
                    "deadline": str(deadline),
                    "duration": (deadline - start).days,
                    "status": "incomplete",
                }
                st.session_state.tasks.append(new_task)
                write_tasks(st.session_state.tasks)
                st.success(msg)
            else:
                st.error(msg)

st.markdown("---")

# Task list
with st.container():
    st.header("Task Manager")
    if st.session_state.tasks:
        for task_data in st.session_state.tasks:
            name, progress, completeBtn, deleteBtn = st.columns([2, 4, 1, 1])

            with name:
                st.write(f'**{task_data["name"]}**')            
            with progress:
                daysLeft = get_days_left(task_data)
                html = progress_bar_chart(task_data)
                st.markdown(html, unsafe_allow_html=True)
                st.write(f'{daysLeft} days left')
            with completeBtn:
                if st.button("Done", key=f'complete_{task_data["name"]}'):
                    task_data["status"] = "complete"
                    write_tasks(st.session_state.tasks)
            with deleteBtn:
                if st.button("Delete", key=f'delete_{task_data["name"]}'):
                    st.session_state.tasks = delete_task(st.session_state.tasks, task_data["name"])
    else:
        st.write("No tasks to display.")
    