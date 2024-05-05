import requests

ENDPOINT = "https://todo.pixegami.io"

def create_task(payload):
    return requests.put(f"{ENDPOINT}/create-task", json=payload)

def update_task(payload):
    return requests.put(f"{ENDPOINT}/update-task", json=payload)

def get_task(task_id):
    return requests.get(f"{ENDPOINT}/get-task/{task_id}")

def list_tasks(user_id):
    return requests.get(f"{ENDPOINT}/list-tasks/{user_id}")

def delete_task(task_id):
    return requests.delete(f"{ENDPOINT}/delete-task/{task_id}")

def check_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code