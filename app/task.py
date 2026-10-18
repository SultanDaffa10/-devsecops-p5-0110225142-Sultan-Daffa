from dataclasses import dataclass


@dataclass
class Task:
    title: str
    description: str = ""
    completed: bool = False

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }