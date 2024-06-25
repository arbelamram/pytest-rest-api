# REST API Testing with Pytest

<!-- Badges -->
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Pytest](https://img.shields.io/badge/Pytest-8.2-green.svg)
![Requests](https://img.shields.io/badge/Requests-2.28-green.svg)
![LICENSE](https://img.shields.io/badge/LICENSE-MIT-black.svg)

### Overview
This project demonstrates how to test a REST API using Pytest.</br>
It includes utility functions to generate task payloads, a wrapper around the ToDo API to facilitate interaction with the endpoints, and a suite of tests to verify the functionality of the API.</br>
Following the principles of OOP, the code is modular, maintainable, and easy to extend.

## Table of Contents
- [Description](#description)
    - [Objectives](#objectives)
    - [Technologies and Tools](#technologies-and-tools)
    - [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
- [Usage](#usage)
    - [Getting Started](#getting-started)
    - [Testing](#testing)
- [Additional Information](#additional-information)
    - [Contributing](#contributing)
    - [Contact](#contact)
    - [Acknowledgments](#acknowledgments)
    - [License](#license)

## Description

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


## Usage

### Getting Started

1. **Prerequisites**:
    * Python 3.12+
    * `pip` (Python package installer)

2. **Clone the Repository**: 
    ```sh
    git clone <repository-url>
    ```

3. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  
    ```
    * On Windows use:
    ```sh
    venv\Scripts\activate
    ```

4. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Set up environment variables**:
    Create a `.env` file in the root directory and add the necessary environment variables:
    ```sh
    TODO_API_BASE_URL=https://todo.pixegami.io
    ```

### Testing
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
    
* Execute a specific test using Pytest:
    ```sh
    pytest-rest-api> python -m pytest -v -s tests\test_todo_api.py::TestToDoAPI::<TEST_NAME>
    
    # Replace <TEST_NAME> with either one of the tests: (CRUD)
        1. test_create_task_variants
        2. test_can_create_task
        3. test_can_read_tasks_list
        4. test_can_update_task_details
        5. test_can_delete_task
    ```



## Additional Information

### Contributing
Contributions to the project are welcome.</br>
Please fork the repository, create a feature branch, and submit a pull request for review.

### Contact

If you have any questions or suggestions, feel free to reach out:

- Email: [ArbelAmram@github.com](mailto:arbelamram@github.com)
- GitHub: [https://github.com/ArbelAmram](https://github.com/ArbelAmram)

### Acknowledgments

- Inspiration:
    * [PyTest REST API Integration Testing with Python](https://www.youtube.com/watch?v=7dgQRVqF1N0)
- Resources:
    * [Badges](https://img.shields.io)

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.