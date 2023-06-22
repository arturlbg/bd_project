## This repository contains a database project for the Database subject using PostgreSQL and Django, with basic Bootstrap for the front-end.

Here we address a vehicle dealership, where you can add and modify: employees, vehicles (available or not for sale), customers, and sales.
Procedures are used in the sales process, and views are used on the sales history screen.

Model:
![image](https://github.com/arturlbg/bd_project/assets/60628919/cbe5a218-d2f4-4d36-ae1e-479238eb8b96)

Some printscreens:
![image](https://github.com/arturlbg/bd_project/assets/60628919/3dd0ec17-0d05-4514-bd63-6ce8da3be71e)
![image](https://github.com/arturlbg/bd_project/assets/60628919/109d60fc-8d66-418c-a964-97d7e5eacbad)
![image](https://github.com/arturlbg/bd_project/assets/60628919/143a3676-c604-4363-a129-e5f0454e4065)


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
