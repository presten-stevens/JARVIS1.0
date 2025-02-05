class task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def __str__(self):
        return f"Task: {self.name}\nDescription: {self.description}\nCompleted: {self.completed}"