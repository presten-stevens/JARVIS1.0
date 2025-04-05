from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class Task:
    title: str
    description: str
    priority: int
    due_date: str
    category: Optional[str] = None
    completed: bool = False
    tags: List[str] = field(default_factory=list)
    id: Optional[int] = None  # Allow initialization to None

    class_id: int = field(init=False, default=0, repr=False)

    def __post_init__(self):
        if self.id is None:
            self.id = Task.class_id
            Task.class_id += 1