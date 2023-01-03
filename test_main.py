from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

data = {
    "task_name": "dummy_task",
    "task_id": 1000

}


def test_tasks_list():
    response = client.get("/tasks_list/")
    assert response.status_code == 200
    assert data in response.json() == {
        "task_id": 1,
        "task_name": "task"
    
    }

def test_get_task():
    response= client.get('/task/{id}',json=data)
    assert response.status_code==200
    assert data in response.json()

def test_add_task():
    response= client.post('/addtask',json=data)
    assert response.status_code==200
    assert data in response.json()

def test_update_task():
    response=client.put('/update/{id}',json=data)
    assert response.status_code==200
    assert data in response.json()

def test_delete_task():
    response=client.delete('/task/{id}',json=data)
    assert response.status_code==200
    assert data in response.json()



