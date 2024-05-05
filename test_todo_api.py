import requests
import uuid

ENDPOINT = "https://todo.pixegami.io"

# Rellevant only at first to check the endpoint connection

# def test_can_call_endpoint():
#     response = requests.get(ENDPOINT)
#     assert response.status_code == 200
    
def test_can_create_task():
    payload = new_task_payload()

    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200

    data = create_task_response.json()

    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]


def test_can_update_task():
    # create a new task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()["task"]["task_id"]

    # update the task
    new_payload = {
        "user_id" : payload["user_id"],
        "task_id" : task_id,
        "content" : "my updated content",
        "is_done" : True,
    }

    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    # get and validate the changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]


def test_can_list_tasks():
    # create N tasks
    N = 3
    payload = new_task_payload()

    for _ in range(N):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    # List tasks, and check that there are N items
    user_id = payload["user_id"]
    list_task_response = list_tasks(user_id)
    assert list_task_response.status_code == 200
    data = list_task_response.json()

    tasks = data["tasks"]
    assert len(tasks) == N


def test_can_delete_task():
    # Create a task.
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    # delete the task.
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    # Get the task, and check that it's not found.
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404


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


def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}" # uuid4 is an object, we want to return a string, therefor .hex 
    content = f"test_content_{uuid.uuid4().hex}"

    return {
        "content": content, # "my test content"
        "user_id": user_id, # "test_user"
        "is_done": False,
    }