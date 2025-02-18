import json
from os import fsencode, listdir
from task import task


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
            if isinstance(object, task):

                data = f"{object.name}~{object.description}"

                with open(self.saveLoc + object.name + ".json", 'w') as file:
                    json.dump(data, file)

    # Load Tasks from JSON
    def load(self):
        for file in listdir(self.saveDir):
            data = json.load(file)
            name, description = data.split("~")
            self.tasks.append(task(name, description))

    def printf(self):
        print(self.tasks)
