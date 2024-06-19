# REST API Testing with Pytest

### Overview
This project demonstrates how to test a REST API using Pytest.</br>
It includes utility functions to generate task payloads, a wrapper around the ToDo API to facilitate interaction with the endpoints, and a suite of tests to verify the functionality of the API.</br>
By following the principles of OOP, the code is modular, maintainable, and easy to extend.</br>

### Table of Contents
- [Objectives](#Objectives)
- [Technologies and Tools](#technologies-and-tools)
- [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Tests](#tests)
- [Contributing](#contributing)

##

### Objectives
* **Automate API Testing**: To automate the process of testing the ToDo API to ensure its endpoints are functioning correctly.</br>
* **Verify CRUD Operations**: To verify that the Create, Read, Update, and Delete operations of the ToDo API work as expected.</br>
* **Demonstrate Pytest Usage**: To demonstrate the use of Pytest for testing REST APIs.</br>
* **Utilize OOP Principles**: To utilize Object-Oriented Programming principles in designing the API wrapper.</br>


### Technologies and Tools
* **Python**: The primary programming language used for writing the API wrapper and tests.</br>
* **Pytest**: A testing framework used for writing and running the tests.</br>
* **Requests**: A Python library for making HTTP requests to interact with the ToDo API.</br>


### Object-Oriented Programming (OOP)
The project employs OOP principles in the design of the `ToDoAPI` class. This approach provides several benefits:

* **Encapsulation**: The ToDoAPI class encapsulates all the methods required to interact with the API, making the code modular and reusable.
* **Abstraction**: The internal workings of the API requests are abstracted away from the test cases, providing a clean and simple interface for interacting with the API.
* **Maintainability**: Any changes to the API endpoints or methods can be managed within the `ToDoAPI` class without affecting the test cases directly.</br>


### Project Structure
The project consists of the following files:

* `test_utils.py`: Utility functions to generate new task payloads.</br>
This module contains utility functions to assist in generating test data.</br>
* `todo_api.py`: A wrapper class to interact with the ToDo API endpoints.</br>
This module contains the ToDoAPI class, which provides methods to interact with the ToDo API.</br>

* `test_todo_api.py`: Test cases written with Pytest to validate the functionality of the ToDo API.</br>
This module contains test cases written using Pytest to validate the functionality of the ToDo API.

##

### Getting Started
* **Clone the Repository**: `git clone <repository-url>`</br>
* **Install Dependencies**: `pip install -r requirements.txt`</br>
* **Configure Environment**: Update test_config.yaml and environment variables.</br>
* **Run Tests**: Execute pytest in the terminal.</br>


### Tests
* **Unit Testing**: PyTest for Python
* **Integration Testing**: Postman for API testing
* **End-to-End Testing**: Selenium for web applications

    ### How to Run the Tests
    1. **Install Dependencies**:
    Ensure you have `pytest` and `requests` installed. You can install them using pip:

        ```sh
        pip install pytest requests
        ```

    2. **Run the Tests**:
    Execute the tests using Pytest:

        ```sh
        pytest test_todo_api.py
        ```

##

### Contributing
Contributions to the project are welcome.</br>
Please fork the repository, create a feature branch, and submit a pull request for review.</br>