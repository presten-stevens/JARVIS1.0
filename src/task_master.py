
# task_master.py
from task import Task

class TaskMaster:
    def __init__(self):
        self.tasks = {}  # Dictionary to store tasks
        self.task_id_counter = 1  # Auto-incrementing counter for task IDs

    def add_task(self, name, description):
        "Add a new task with a unique ID."
        new_task = Task(name, description)
        task_id = self.task_id_counter
        self.tasks[task_id] = new_task
        self.task_id_counter += 1
        print(f"Task added with ID: {task_id}")

    def delete_task(self, task_id):
        "Delete a task by its ID."
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task with ID {task_id} deleted.")
        else:
            print(f"Task with ID {task_id} not found.")

    def view_tasks(self):
        "Print all tasks along with their unique IDs."
        if not self.tasks:
            print("No tasks available.")
            return
        print("*" * 20)
        print("Current Tasks:")
        print("*" * 20)
        for task_id, task in self.tasks.items():
            print(f"ID: {task_id}")
            print(f"Name: {task.name}")
            print(f"Description: {task.description}")
            print("-" * 20)

    # Save Tasks as JSON

    # Load Tasks from JSON