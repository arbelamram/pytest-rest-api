import uuid

def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"

    return {
        "content": content,
        "user_id": user_id,
        "is_done": False,
    }