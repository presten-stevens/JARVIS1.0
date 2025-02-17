class Task:
    def __init__(self, name: str, description: str, priority: int,
                dueDate: str, category: str, completed: bool = False):
        self.name = name
        self.description = description
        self.priority = priority
        self.dueDate = dueDate
        self.category = category
        self.completed = completed

    def __str__(self):
        return (f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Priority: {self.priority}\n"
            f"Due Date: {self.dueDate}\n"
            f"Category: {self.category}\n"
            f"Completed: {self.completed}\n"
        )
    
    def setName(self, name):
        self.name = name

    def setDescription(self, description: str):
        self.description = description

    def setPriority(self, priority: int):
        self.priority = priority

    def setDueDate(self, dueDate: str):
        self.dueDate = dueDate

    def setCategory(self, category: str):
        self.category = category

    def setCompleted(self, completed: bool):
        self.completed = completed
