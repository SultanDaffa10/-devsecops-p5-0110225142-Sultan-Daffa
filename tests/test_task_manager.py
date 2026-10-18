import pytest

from app.task_manager import TaskManager


def test_add_task():
    manager = TaskManager()
    task = manager.add_task("Complete assignment", "DevSecOps")

    assert task.title == "Complete assignment"
    assert len(manager.get_tasks()) == 1


def test_complete_task():
    manager = TaskManager()
    manager.add_task("Run unit tests")

    task = manager.complete_task(0)

    assert task.completed is True


def test_complete_task_rejects_invalid_index():
    manager = TaskManager()

    with pytest.raises(IndexError):
        manager.complete_task(0)


def test_complete_task_rejects_boolean_index():
    manager = TaskManager()
    manager.add_task("Run security scan")

    with pytest.raises(TypeError):
        manager.complete_task(True)