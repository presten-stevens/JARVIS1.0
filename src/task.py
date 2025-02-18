class task:
    def __init__(self, name, description, completed=False):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Task: {self.name}\nDescription: {self.description}\nCompleted: {self.completed}"

    def __repr__(self):
        return self.name