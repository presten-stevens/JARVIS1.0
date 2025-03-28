import json
# from os import fsencode, listdir, makedirs
import os
from task import Task

class TaskMaster:
    def __init__(self, saveLoc = "saves/"):
        self.tasks = {}  # Dictionary to store tasks
        self.save_loc = 'saves/'
        self.save_dir = os.fsencode(self.save_loc)

    def add_task(self, title: str, description: str, priority: int,
                due_date: str, category: str, completed: bool = False):
        """"
            Add a new task with a unique ID.
        """
        new_task = Task(title, description, priority, due_date, category, completed)
        self.tasks[new_task.id] = new_task
        print(f"Task added with ID: {new_task.id}")

    def delete_task(self, task_id):
        """"
            Delete a task by its ID.
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task with ID {task_id} deleted.")
        else:
            print(f"Task with ID {task_id} not found.")

    def view_tasks(self):
        """"
            Print all tasks along with their unique IDs.
        """
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
        os.makedirs(self.save_loc, exist_ok=True)

        #iterate through id and object pairs
        for id, object in self.tasks.items():

            if isinstance(object, Task):

                #dump task data to file
                with open(self.save_loc + str(id) + "-" + object.title.replace(" ", "-") + ".json", 'w') as file:
                    json.dump(object.to_dict(), file)

    # Load Tasks from JSON
    def load(self):
        #Verify that the path exists
        if not os.path.exists(self.save_loc):
            os.makedirs(self.save_loc, exist_ok=True)
            return

        #Clear task dictionary
        self.tasks = {}

        #Iterate through files
        for file_path in os.listdir(self.save_dir):

            #convert path to str
            file_path = str(file_path)

            #open file in read mode
            with open(self.save_loc + file_path[2:-1], 'r') as file:
                #load file data
                data = json.load(file)

                #create task from data dictionary
                task = Task.from_dict(data)

                #assign id/task key/value pair
                self.tasks[task.id] = task

        #Adjust counting ID for Task class
        Task.set_class_id(max(self.tasks.keys()) + 1)

    def printf(self):
        print(self.tasks)

    # Edit Tasks
    def edit_task(self, task_id: int, target_var: str, revision: str):
        if task_id not in self.tasks:
            raise Exception(f"Task ID#'{task_id}' not found")
        
        task = self.tasks[task_id]

        target_var = target_var.lower()
        if target_var not in vars(task).keys():
            raise Exception(f"Variable '{target_var}' not valid Task attribute")
        
        setattr(task, target_var, revision)
        print(task)

    def get_task(self, task_id: int):
        return self.tasks[task_id]
    
    def get_tasks(self):
        return self.tasks