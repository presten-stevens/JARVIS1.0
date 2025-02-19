class Task:
    def __init__(self, title: str, description: str, priority: int,
                dueDate: str, category: str, completed: bool = False):
        self.title = title
        self.description = description
        self.priority = priority
        self.dueDate = dueDate
        self.category = category
        self.completed = completed

    def __str__(self):
        return (f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Priority: {self.priority}\n"
            f"Due Date: {self.dueDate}\n"
            f"Category: {self.category}\n"
            f"Completed: {self.completed}\n"
        )
    
    def setTitle(self, title):
        self.title = title

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
