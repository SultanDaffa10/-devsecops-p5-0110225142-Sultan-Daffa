import pytest

from app.task import Task
from app.validators import validate_title


def test_task_can_be_completed():
    task = Task(title="Learn DevSecOps")
    task.mark_completed()

    assert task.completed is True


def test_task_to_dict():
    task = Task(title="Learn Python", description="Practice")
    result = task.to_dict()

    assert result["title"] == "Learn Python"
    assert result["completed"] is False


def test_validate_title_removes_extra_spaces():
    assert validate_title("  Study Python  ") == "Study Python"


@pytest.mark.parametrize("title", ["", "   "])
def test_validate_title_rejects_empty_input(title):
    with pytest.raises(ValueError):
        validate_title(title)