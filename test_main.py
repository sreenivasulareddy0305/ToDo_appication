from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app=app)

data = [{
    "task_name": "dummy_task",
    "task_id": 1000

}]


def test_index():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK


def test_tasks_list():
    response = client.get("/tasks_list/")
    assert response.status_code == status.HTTP_200_OK


def test_get_task():
    response = client.get('/task/{0}')
    assert response.status_code == status.HTTP_200_OK


def test_add_task():
    response = client.post(
        '/addtask', json={"task_id": 22, "task_name": "task"})
    assert response.status_code == status.HTTP_201_CREATED


def test_update_task():
    response = client.put(
        '/update/{id}', json={"task_id": 0, "task_name": "task"})
    assert response.status_code == status.HTTP_200_OK


def test_delete_task():
    response = client.delete('/task/{id}')
    assert response.status_code == 200
    # assert data in response.json() == data
