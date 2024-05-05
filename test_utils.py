import uuid

def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}" # uuid4 is an object, we want to return a string, therefor .hex 
    content = f"test_content_{uuid.uuid4().hex}"

    return {
        "content": content, # "my test content"
        "user_id": user_id, # "test_user"
        "is_done": False,
    }