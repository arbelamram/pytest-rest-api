import requests

class ToDoAPI:
    BASE_URL = "https://todo.pixegami.io"

    def __init__(self):
        self.session = requests.Session()
    
    def _request(self, method, endpoint, **kwargs):
        url = f"{self.BASE_URL}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json() if response.content else None

    def create_task(self, payload):
        return self._request('PUT', '/create-task', json=payload)

    def get_task(self, task_id):
        return self._request('GET', f'/get-task/{task_id}')

    def get_tasks_list(self, user_id):
        return self._request('GET', f'/list-tasks/{user_id}')

    def update_task_details(self, payload):
        return self._request('PUT', '/update-task', json=payload)
    
    def delete_task(self, task_id):
        self._request('DELETE', f'/delete-task/{task_id}')
