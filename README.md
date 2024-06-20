# REST API Testing with Pytest

### Overview
This project demonstrates how to test a REST API using Pytest.</br>
It includes utility functions to generate task payloads, a wrapper around the ToDo API to facilitate interaction with the endpoints, and a suite of tests to verify the functionality of the API.</br>
By following the principles of OOP, the code is modular, maintainable, and easy to extend.

### Table of Contents
- [Objectives](#Objectives)
- [Technologies and Tools](#technologies-and-tools)
- [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Tests](#tests)
- [Contributing](#contributing)
- [License](#license)

##

### Objectives
* **Automate API Testing**: To automate the ToDo API testing process to ensure its endpoints function correctly.
* **Verify CRUD Operations**: To verify that the Create, Read, Update, and Delete operations of the ToDo API work as expected.
* **Demonstrate Pytest Usage**: To demonstrate the use of Pytest for testing REST APIs.
* **Utilize OOP Principles**: To utilize Object-Oriented Programming principles in designing the API wrapper.


### Technologies and Tools
* **Python**: The primary programming language used for writing the API wrapper and tests.
* **Pytest**: A testing framework used for writing and running the tests.
* **Requests**: A Python library for making HTTP requests to interact with the ToDo API.


### Object-Oriented Programming (OOP)
The project employs OOP principles in the design of the `ToDoAPI` class.</br>
This approach provides several benefits:

* **Encapsulation**: The ToDoAPI class encapsulates all the methods required to interact with the API, making the code modular and reusable.
* **Abstraction**: The internal workings of the API requests are abstracted away from the test cases, providing a clean and simple interface for interacting with the API.
* **Maintainability**: Any changes to the API endpoints or methods can be managed within the `ToDoAPI` class without affecting the test cases directly.


### Project Structure
The project consists of the following files:

* `todo_api.py`: A wrapper class to interact with the ToDo API endpoints.</br>
* `tests/test_utils.py`: Utility functions to generate new task payloads.</br>
* `tests/test_todo_api.py`: Test cases written with Pytest to validate the functionality of the ToDo API.</br>

##

### Getting Started
**Prerequisites**:
* Python 3.7+
* `pip` (Python package installer)

**Clone the Repository**: `git clone <repository-url>`

**Create a virtual environment**:
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**Install Dependencies**: `pip install -r requirements.txt`</br>

**Set up environment variables**:</br>
Create a .env file in the root directory and add the necessary environment variables:
```sh
TODO_API_BASE_URL=https://todo.pixegami.io
# You may replace with any API base URL
```

### Tests
* **Unit Testing**: PyTest for Python
* **Integration Testing**: Postman for API testing
* **End-to-End Testing**: Selenium for web applications

#### How to Run the Tests
1. **Install Dependencies**:
Ensure you have `pytest` and `requests` installed.</br>
You can install them using pip:

    ```sh
    pip install pytest requests
    ```

2. **Run the Tests**:
* Execute all the tests **consecutively** using Pytest:
    ```sh
    pytest-rest-api> python -m pytest -v -s tests\test_todo_api.py
    ```
    
* Execute a specific single test using Pytest:
    ```sh
    pytest-rest-api> python -m pytest -v -s tests\test_todo_api.py::TestToDoAPI::<TEST_NAME>
    
    # Replace <TEST_NAME> with either one of the tests: (CRUD)
        1. test_create_task_variants
        2. test_can_create_task
        3. test_can_read_tasks_list
        4. test_can_update_task_details
        5. test_can_delete_task
    ```

##

### Contributing
Contributions to the project are welcome.</br>
Please fork the repository, create a feature branch, and submit a pull request for review.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.