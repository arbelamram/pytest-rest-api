import pytest
from tasks import ToDoAPI
from test_utils import new_task_payload

class TestToDoAPI():
    @pytest.fixture(scope="class")
    def api_instance(self):
        return ToDoAPI()

    def test_can_create_task(self, api_instance):
        payload = new_task_payload()
        create_task_response = api_instance.create_task(payload)
        task_id = create_task_response["task"]["task_id"]
        get_task_response = api_instance.get_task(task_id)
        get_task_data = get_task_response

        assert get_task_data["content"] == payload["content"]
        assert get_task_data["user_id"] == payload["user_id"]

    def test_can_list_tasks(self, api_instance):
            N = 3
            payload = new_task_payload()

            for _ in range(N):
                api_instance.create_task(payload)

            user_id = payload["user_id"]
            list_task_response = api_instance.get_tasks_list(user_id)
            data = list_task_response

            tasks = data["tasks"]
            assert len(tasks) == N

    def test_can_update_task_details(self, api_instance):
        payload = new_task_payload()
        create_task_response = api_instance.create_task(payload)
        task_id = create_task_response["task"]["task_id"]

        new_payload = {
            "user_id" : payload["user_id"],
            "task_id" : task_id,
            "content" : "my updated content",
            "is_done" : True,
        }

        api_instance.update_task_details(new_payload)

        get_task_response = api_instance.get_task(task_id)
        get_task_data = get_task_response

        assert get_task_data["content"] == new_payload["content"]
        assert get_task_data["is_done"] == new_payload["is_done"]

    def test_can_delete_task(self, api_instance):
        payload = new_task_payload()
        create_task_response = api_instance.create_task(payload)
        task_id = create_task_response["task"]["task_id"]

        api_instance.delete_task(task_id)
