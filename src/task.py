class Task:
    def __init__(self, name, description, completed=False):
        self.name = name
        self.description = description
        self.completed = completed

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}"
