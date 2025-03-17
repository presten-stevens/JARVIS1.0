import json
from os import fsencode, listdir
from task import Task

class TaskMaster:
    def __init__(self, saveLoc = "saves/"):
        self.tasks = {}  # Dictionary to store tasks
        self.task_id_counter = 1  # Auto-incrementing counter for task IDs
        self.saveLoc = saveLoc
        self.saveDir = fsencode(self.saveLoc)

    def add_task(self, title: str, description: str, priority: int,
                dueDate: str, category: str, completed: bool = False):
        "Add a new task with a unique ID."
        new_task = Task(title, description, priority, dueDate, category, completed)
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
            print(f"Name: {task.title}")
            print(f"Description: {task.description}")
            print("-" * 20)

    # Save Tasks as JSON
    def save(self):
        for object in self.tasks.values():
            if isinstance(object, Task):
                with open(self.saveLoc + object.title.replace(" ", "-") + ".json", 'w') as file:
                    json.dump(object.to_dict(), file)

    # Load Tasks from JSON
    def load(self):
        self.tasks = {}
        for id, file_path in enumerate(listdir(self.saveDir)):
            file_path = str(file_path)
            self.task_id_counter = id + 1
            with open(self.saveLoc + file_path[2:-1], 'r') as file:  # Open the file in read mode
                data = json.load(file)  # Load the JSON data from the file
                self.tasks[self.task_id_counter] = Task.from_dict(data)
        self.task_id_counter += 1


    def printf(self):
        print(self.tasks)


    # Edit Tasks
    def editTask(self, task_id: int, target_var: str, revision: str):
        if task_id not in self.tasks:
            raise Exception(f"Task ID#'{task_id}' not found")
        
        task = self.tasks[task_id]

        target_var = target_var.lower()
        if target_var not in vars(task).keys():
            raise Exception(f"Variable '{target_var}' not valid Task attribute")
        
        setattr(task, target_var, revision)
        print(task)
