import json
import os
from task import Task

class TaskMaster:
    def __init__(self, saveLoc = 'saves/tasks/', sortmode = "PRIORITY"):
        self.tasks = {}  
        self.save_loc = saveLoc
        self.save_dir = os.fsencode(self.save_loc)
        self.SORTMODE = sortmode

    def add_task(self, new_task: Task):
        """
            Add a new task with a unique ID.
        """
        self.tasks[new_task.id] = new_task
        print(f"Task added with ID: {new_task.id}")

    def delete_task(self, task_id):
        """"
            Delete a task by its ID. And delete it from the save folder
        """
        task = self.get_task(task_id)
        if not task: 
            return
        del self.tasks[task_id]
        print(f"Task with ID {task_id} deleted.")


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

    def update_task_with_tag(self, task_id: int, tag: str):
        """
            Updates a given task (by ID) to have an additional tag
        """
        task = self.get_task(task_id)
        print(task.tags)
        if tag not in task.tags:
            task.add_tag(tag)
            print(f"Task '{task.title}' updated with tag: {tag}")
        else:
            print(f"Task '{task.title}' already has tag: {tag}")
        

    # Save Tasks as JSON
    def save(self):
        os.makedirs(self.save_loc, exist_ok=True)

        #clear directory and rewrite each task including edits to new files
        for item in os.listdir(self.save_loc):
            file_path = os.path.join(self.save_loc, item)

            if os.path.isfile(file_path):
                os.remove(file_path)

        #iterate through id and object pairs
        for id, object in self.tasks.items():

            #dump task data to file
            with open(self.save_loc + str(object.id) + "-" + object.title.replace(" ", "-") + ".json", 'w') as file:
                json.dump(object.to_dict(), file)
        print("Saved")

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
        if len(self.tasks) > 0:
            Task.set_class_id(max(self.tasks.keys()) + 1)
        else:
            Task.set_class_id(0)

    def printf(self):
        print(self.tasks)

    # Edit Tasks
    def edit_task(self, task_id: int, target_var: str, revision: str):
        """
            Edits a task given its id, the variable you want to change, and the desired value
        """
        if task_id not in self.tasks:
            raise Exception(f"Task ID#'{task_id}' not found")

        task = self.tasks[task_id]

        target_var = target_var.lower()
        if target_var not in vars(task).keys():
            raise Exception(f"Variable '{target_var}' not valid Task attribute")

        setattr(task, target_var, revision)

    def get_task(self, task_id: int):
        """
            Returns task from ID
        """
        if task_id in self.tasks.keys():
            return self.tasks[task_id]
        else:
            print(f"Task with ID {task_id} not found.")

    def get_tasks(self):
        return self.tasks
    
    # Filter Tasks
    def filter_tasks_by_priority(self, priority):
        """
            Returns a list of tasks with the given priority.
        """
        return [task for task in self.tasks if task.priority == priority]
    
    def filter_tasks_by_tag(self, tag):
        """
            Return a list of tasks that contain the given tag.
        """
        return [task for task in self.tasks if tag in task.tags]
    
    def get_tags(self):
        """
            Returns a list of all current tags for tasks 
        """
        tags = ["None"]
        for task in self.tasks.values():
            for tag in task.tags:
                if tag not in tags:
                    tags.append(tag)
        return tags

    def sort_tasks(self):
        """
            Returns the tasks sorted by SORTMODE
        """
        sortdict = {"PRIORITY": lambda x: x.priority}
        return sorted(self.get_tasks().values(), key = sortdict[self.SORTMODE])

