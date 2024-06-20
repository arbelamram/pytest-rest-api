import os
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ToDoAPI:
    def __init__(self):
        self.BASE_URL = os.getenv("TODO_API_BASE_URL")
        if self.BASE_URL is None:
            raise ValueError("The TODO_API_BASE_URL environment variable is not set.")
        
        self.session = requests.Session()
        retries = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504])
        self.session.mount('http://', HTTPAdapter(max_retries=retries))
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.BASE_URL}{endpoint}"
        kwargs.setdefault('timeout', 10)
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json() if response.content else None
        except requests.exceptions.RequestException as e:
            if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 404:
                logger.warning(f"Resource not found: {url}")
                return None
            logger.error(f"Request failed: {e}")
            raise

    def create_task(self, payload):
        return self._request('PUT', '/create-task', json=payload)

    def get_task(self, task_id):
        return self._request('GET', f'/get-task/{task_id}')

    def get_tasks_list(self, user_id):
        return self._request('GET', f'/list-tasks/{user_id}')

    def update_task_details(self, payload):
        return self._request('PUT', '/update-task', json=payload)

    def delete_task(self, task_id):
        response = self._request('DELETE', f'/delete-task/{task_id}')
        if response is None:
            return True  # Task not found, assume deleted
        if 'error' in response:
            logger.error(f"Error deleting task: {response['error']}")
            raise requests.exceptions.HTTPError(response['error'])
        return True  # Explicitly returning True if deletion was successful