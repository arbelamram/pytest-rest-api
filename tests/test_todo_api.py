import pytest
import requests
import time

from dotenv import load_dotenv

from todo_api import ToDoAPI
from test_utils import new_task_payload

# Load environment variables from .env file
load_dotenv()

class DataHelper:
    def __init__(self, api_instance):
        self.api_instance = api_instance
        self.created_task_ids = []

    def create_task(self, payload):
        response = self.api_instance.create_task(payload)
        self.created_task_ids.append(response["task"]["task_id"])
        return response

    def cleanup(self):
        for task_id in self.created_task_ids:
            self.api_instance.delete_task(task_id)
        self.created_task_ids = []

class TestToDoAPI:
    @pytest.fixture(scope="class")
    def api_instance(self):
        return ToDoAPI()

    @pytest.fixture(scope="class")
    def data_helper(self, api_instance):
        helper = DataHelper(api_instance)
        yield helper
        helper.cleanup()

    @pytest.fixture
    def task_payload(self):
        return new_task_payload()

    def _wait_for_condition(self, condition_func, max_attempts=3, delay=1):
        """Poll the server until the condition_func returns True."""
        for _ in range(max_attempts):
            if condition_func():
                return True
            time.sleep(delay)
        return False

    @pytest.mark.parametrize("task_payload", [new_task_payload()])
    def test_create_task_variants(self, api_instance, task_payload):
        response = api_instance.create_task(task_payload)
        assert response is not None
        task_id = response["task"]["task_id"]
        
        get_task_data = api_instance.get_task(task_id)
        assert get_task_data["content"] == task_payload["content"]
        assert get_task_data["user_id"] == task_payload["user_id"]
        
        # Cleanup
        api_instance.delete_task(task_id)

    def test_can_create_task(self, api_instance, task_payload, data_helper):
        try:
            response = data_helper.create_task(task_payload)
            assert response is not None
            task_id = response["task"]["task_id"]
        
            get_task_data = api_instance.get_task(task_id)
            assert get_task_data["content"] == task_payload["content"]
            assert get_task_data["user_id"] == task_payload["user_id"]
        finally:
            data_helper.cleanup()

    def test_can_read_tasks_list(self, api_instance, task_payload, data_helper):
        user_id = task_payload["user_id"]

        for _ in range(3):
            data_helper.create_task(task_payload)

        list_task_response = api_instance.get_tasks_list(user_id)
        tasks = list_task_response["tasks"]
        assert len(tasks) == 3

        data_helper.cleanup()

    def test_can_update_task_details(self, api_instance, task_payload, data_helper):
        create_response = data_helper.create_task(task_payload)
        task_id = create_response["task"]["task_id"]

        new_payload = {
            "user_id": task_payload["user_id"],
            "task_id": task_id,
            "content": "my updated content",
            "is_done": True,
        }

        api_instance.update_task_details(new_payload)
        get_task_data = api_instance.get_task(task_id)
        assert get_task_data["content"] == new_payload["content"]
        assert get_task_data["is_done"] == new_payload["is_done"]

        data_helper.cleanup()

    def test_can_delete_task(self, api_instance, task_payload, data_helper):
        create_response = data_helper.create_task(task_payload)
        task_id = create_response["task"]["task_id"]

        # Ensure the task exists before deletion
        try:
            api_instance.get_task(task_id)
        except requests.exceptions.HTTPError:
            pytest.fail(f"Task {task_id} does not exist before deletion attempt")

        # Attempt to delete the task
        api_instance.delete_task(task_id)

        # Poll to ensure the task is deleted
        condition_func = lambda: api_instance.get_task(task_id) is None
        task_deleted = self._wait_for_condition(condition_func)
        assert task_deleted, f"Task {task_id} was not deleted after multiple attempts"