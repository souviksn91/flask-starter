# Flask Starter Template
A reusable Flask starter template built for rapid project setup, backend development, and experimentation. 


## Features

- Flask 3.x
- Application Factory Pattern
- Blueprint Architecture
- SQLAlchemy ORM
- Flask-Migrate (Alembic)
- MySQL Database Support
- Environment Variables with python-dotenv
- UV for dependency and virtual environment management
- Modular project structure
- Starter template and base HTML layout

## Tech Stack

- Python 3.13.12
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- PyMySQL
- python-dotenv
- UV
- MySQL

## Setup
- git clone repository-url 
- cd flask-starter
- uv sync
- source .venv/bin/activate
- python --version
- Create a .env file in the project root, copy from .env.example, and replace the credentials with your own MySQL username, password, and database name.
- Open MySQL Workbench or connect through the terminal and create the database: **CREATE DATABASE flasktest_db;**
- uv run flask --app app.py db upgrade
- uv run python app.py 
- Visit: http://127.0.0.1:8000/


**Creating New Migrations (after modifying models):**

- uv run flask --app app.py db migrate -m "Describe your changes"
- uv run flask --app app.py db upgrade