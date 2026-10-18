from app.task import Task
from app.validators import validate_title


class TaskManager:
    def __init__(self):
        self._tasks = []

    def add_task(self, title: str, description: str = "") -> Task:
        task = Task(
            title=validate_title(title),
            description=description.strip(),
        )
        self._tasks.append(task)
        return task

    def get_tasks(self):
        return list(self._tasks)

    def complete_task(self, index: int) -> Task:
        if not isinstance(index, int) or isinstance(index, bool):
            raise TypeError("Task index must be an integer.")

        if index < 0 or index >= len(self._tasks):
            raise IndexError("Task index does not exist.")

        task = self._tasks[index]
        task.mark_completed()
        return task