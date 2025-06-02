import pytest
from starlette.testclient import TestClient


@pytest.mark.parametrize(
    "payload",
    [
        {"title": "Test 1", "completed": False},
        {"title": "Buy milk", "completed": True},
    ],
)

# Проверяем, что post /api/tasks возвращает созданную задачу с правилными полями
def test_create_task(client: TestClient, payload: dict) -> None:
    """ """
    response = client.post("/api/tasks", json=payload)
    assert response.status_code == 201 or response.status_code == 200
    data: dict = response.json()
    assert isinstance(data, dict)
    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["completed"] == payload["completed"]


# сначала создаём задачу, затем проверяем, что GET /api/tasks возвращает список, содержащий как минимум эту задачу.
def test_read_tasks(client: TestClient) -> None:
    # создаём задачу
    client.post("/api/tasks", json={"title": "First Task", "completed": False})

    # получаем спиисок
    response = client.get("/api/tasks")
    assert response.status_code == 200
    data: list[dict] = response.json()

    assert isinstance(data, list)
    assert len(data) >= 1

    first = data[0]
    assert "id" in first and isinstance(first["id"], int)
    assert "title" in first and isinstance(first["title"], str)
    assert "completed" in first and isinstance(first["completed"], bool)
