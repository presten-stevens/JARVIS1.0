from task import Task

class Taskmaster:
    def __init__(self):
        self.tasks = {}
    
    # Add a task
    
    # Delete a task

    # View all tasks

    # Save Tasks as JSON

    # Load Tasks from JSON

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
