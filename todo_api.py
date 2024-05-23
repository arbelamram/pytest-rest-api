import requests

class ToDoAPI:
    BASE_URL = "https://todo.pixegami.io"
        
    def create_task(self, payload):
        create_task_response = requests.put(f"{self.BASE_URL}/create-task", json=payload)
        create_task_response.raise_for_status()
        return create_task_response.json()

    def get_task(self, task_id):
        response = requests.get(f"{self.BASE_URL}/get-task/{task_id}")
        response.raise_for_status()
        return response.json()

    def get_tasks_list(self, user_id):
        response = requests.get(f"{self.BASE_URL}/list-tasks/{user_id}")
        response.raise_for_status()
        return response.json()

    def update_task_details(self, payload):
            response = requests.put(f"{self.BASE_URL}/update-task", json=payload)
            response.raise_for_status()
            return response.json()
    
    def delete_task(self, task_id):
        delete_task_response = requests.delete(f"{self.BASE_URL}/delete-task/{task_id}")
        delete_task_response.raise_for_status()

        get_task_response = requests.get(f"{self.BASE_URL}/get-task/{task_id}")
        assert get_task_response.status_code == 404