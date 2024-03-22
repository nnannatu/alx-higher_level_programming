# Python Object-Relational Mapping (ORM) Project

## Overview
This project aims to demonstrate the seamless integration of Python with MySQL databases using both raw SQL queries and Object-Relational Mapping (ORM) techniques. By utilizing the MySQLdb module and SQLAlchemy ORM library, developers can effectively interact with MySQL databases, perform CRUD operations, and manipulate data without directly writing SQL queries.

## Getting Started
To set up your development environment and execute the project, follow these steps:

### Prerequisites
- Python 3.8.x
- MySQL server 8.0
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x

### Installation
1. Install Python 3.8 if not already installed.
2. Install and activate a Python virtual environment (venv):
    ```bash
    $ sudo apt-get install python3.8-venv
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
3. Install MySQLdb module version 2.0.x:
    ```bash
    $ sudo apt-get install python3-dev
    $ sudo apt-get install libmysqlclient-dev
    $ sudo apt-get install zlib1g-dev
    $ sudo pip3 install mysqlclient
    ```
4. Install SQLAlchemy module version 1.4.x:
    ```bash
    $ sudo pip3 install SQLAlchemy
    ```

### Usage
- Ensure your MySQL server is running.
- Execute Python scripts provided in the project to perform database operations using either raw SQL queries or SQLAlchemy ORM.

### File Structure
- `raw_sql_operations.py`: Demonstrates database operations using raw SQL queries.
- `orm_operations.py`: Demonstrates database operations using SQLAlchemy ORM.
- `README.md`: Project documentation.

## Learning Objectives
Upon completion of this project, you will gain proficiency in the following areas:
- Connecting to a MySQL database from a Python script.
- Performing SELECT, INSERT, UPDATE, DELETE operations in a MySQL table using Python.
- Understanding the concept of Object-Relational Mapping (ORM) and its benefits.
- Mapping Python classes to MySQL tables using SQLAlchemy ORM.
- Creating and activating Python virtual environments for project isolation.

## Additional Resources
- [MySQLdb Documentation](https://mysqlclient.readthedocs.io/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)
- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/21/orm/tutorial.html)

## Author
[Your Name]

## License
This project is licensed under the [MIT License](LICENSE).
