class Task:
    class_id = 0

    def __init__(self, title: str, description: str, priority: int,
                due_date: str, category: str = None, completed: bool = False, tags: list = None, id = None):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.category = category
        self.completed = completed
        self.tags = tags if tags else []
        if id == None:
            self.id = Task.class_id
        else:
            self.id = id
        Task.class_id += 1

    def __str__(self):
        return (f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Priority: {self.priority}\n"
            f"Due Date: {self.due_date}\n"
            f"Category: {self.category}\n"
            f"Completed: {self.completed}\n"
            f"Tags: {', '.join(self.tags)}\n"
            f"Id: {self.id}"
        )

    def __repr__(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def set_description(self, description: str):
        self.description = description

    def set_priority(self, priority: int):
        self.priority = priority

    def set_due_date(self, due_date: str):
        self.due_date = due_date

    def set_category(self, category: str):
        self.category = category

    def set_completed(self, completed: bool):
        self.completed = completed

    def add_tag(self, tags: str):
        if tags not in self.tags:
            self.tags.append(tags)

    def remove_tag(self, tags: str):
        if tags in self.tags:
            self.tags.remove(tags)

    def set_id(self, id: int):
        self.id = id

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date,
            'category': self.category,
            'completed': self.completed,
            'tags': self.tags,
            'id': self.id
        }

    # Method to create a Task instance from a dictionary
    @classmethod
    def from_dict(cls, task_dict):
        return cls(
            task_dict['title'],
            task_dict['description'],
            task_dict['priority'],
            task_dict['due_date'],
            task_dict['category'],
            task_dict['completed'],
            task_dict.get('tags', []),
            task_dict['id']
        )

    @classmethod
    def set_class_id(cls, other: int):
        cls.class_id = other