import pytest


@pytest.mark.parametrize(
    "task_data",
    [
        {"title": "Test 1", "completed": False},
        {"title": "Buy milk", "completed": True},
    ],
)
def test_create_task(client, task_data):
    pass


def test_read_tasks(client):
    pass
