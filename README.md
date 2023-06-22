**This repository contains a database project for the Database subject using PostgreSQL and Django, 
with basic Bootstrap for the front-end.**

Here we address a vehicle dealership, where you can add and modify: employees, vehicles (available or not for sale), customers, and sales.
Procedures are used in the sales process, and views are used on the sales history screen.

The project covered the following topics:
- Most SQL Statements
- Procedures
- Views

**Installation**

To set up the Django Database Project locally, follow these steps:

Clone the repository to your local machine using the following command:

```git clone https://github.com/arturlbg/bd_project.git```

Navigate to the project directory:

```cd bd_project```

Create a virtual environment to isolate project dependencies:

```python3 -m venv venv```

Activate the virtual environment:

For Windows:

```venv\Scripts\activate```

For macOS and Linux:

```source venv/bin/activate```

Install the required dependencies:

- Python 3.10 or higher
- PostgreSQL
- Django framework

Perform the initial database setup and migrations:

```python manage.py makemigrations```
```python manage.py migrate```

Start the development server:

```python manage.py runserver```

Access the project in your web browser at http://localhost:8000.
