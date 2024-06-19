import pytest
import requests

from todo_api import ToDoAPI
from test_utils import new_task_payload

class TestToDoAPI:
    @pytest.fixture(scope="class")
    def api_instance(self):
        return ToDoAPI()

    @pytest.fixture
    def task_payload(self):
        return new_task_payload()

    @pytest.fixture
    def created_task(self, api_instance, task_payload):
        create_task_response = api_instance.create_task(task_payload)
        task_id = create_task_response["task"]["task_id"]
        return task_id, task_payload

    def test_can_create_task(self, api_instance, created_task):
        task_id, payload = created_task
        get_task_data = api_instance.get_task(task_id)

        assert get_task_data["content"] == payload["content"]
        assert get_task_data["user_id"] == payload["user_id"]

    def test_can_read_tasks_list(self, api_instance, task_payload):
        N = 3
        user_id = task_payload["user_id"]

        # Create N tasks
        for _ in range(N):
            api_instance.create_task(task_payload)

        list_task_response = api_instance.get_tasks_list(user_id)
        tasks = list_task_response["tasks"]

        assert len(tasks) == N

    def test_can_update_task_details(self, api_instance, created_task):
        task_id, payload = created_task

        new_payload = {
            "user_id": payload["user_id"],
            "task_id": task_id,
            "content": "my updated content",
            "is_done": True,
        }

        api_instance.update_task_details(new_payload)

        get_task_data = api_instance.get_task(task_id)

        assert get_task_data["content"] == new_payload["content"]
        assert get_task_data["is_done"] == new_payload["is_done"]

    def test_can_delete_task(self, api_instance, created_task):
        task_id, _ = created_task

        api_instance.delete_task(task_id)

        with pytest.raises(requests.exceptions.HTTPError) as excinfo:
            api_instance.get_task(task_id)
        assert excinfo.value.response.status_code == 404