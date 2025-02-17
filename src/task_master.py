from typing import List
from task import Task

class Taskmaster:
    def __init__(self):
        self.tasks: List[Task] = []
    
    # Add a task
    
    # Delete a task

    # View all tasks

    # Save Tasks as JSON

    # Load Tasks from JSON

    def _getTask(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                return task
        return None

    # Edit Tasks
    def editTask(self, task_name: str, target_var: str, revision: str):
        task = self._getTask(task_name)

        if not task:
            raise Exception(f"Task '{task_name}' not found")
        
        target_var = target_var.lower()
        if target_var not in vars(task).keys():
            raise Exception(f"Variable '{target_var}' not valid Task attribute")
        
        setattr(task, target_var, revision)
        print(task)
