import json
from os import fsencode, listdir
from task import Task


class task_master:
    def __init__(self):
        self.tasks = []
        self.saveLoc = 'saves/'
        self.saveDir = fsencode(self.saveLoc)
    
    # Add a task
    
    # Delete a task

    # View all tasks

    # Save Tasks as JSON
    def save(self):
        for object in self.tasks:
            if isinstance(object, Task):

                with open(self.saveLoc + object.title + ".json", 'w') as file:
                    json.dump(object.to_dict(), file)

    # Load Tasks from JSON
    def load(self):
        self.tasks = []
        for file_path in listdir(self.saveDir):
            file_path = str(file_path)
            with open(self.saveLoc + file_path[2:-1], 'r') as file:  # Open the file in read mode
                data = json.load(file)  # Load the JSON data from the file
                self.tasks.append(Task.from_dict(data))


    def printf(self):
        print(self.tasks)
