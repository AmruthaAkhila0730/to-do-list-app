# Flask To-Do List Application

A simple To-Do list application built using Flask and SQLAlchemy.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)

## Introduction

This project is a basic To-Do list application developed with Flask, a lightweight Python web framework, and SQLAlchemy, an SQL toolkit and Object-Relational Mapping (ORM) library. It allows users to add, edit, complete, and remove tasks, with tasks stored in a SQLite database (`tasks.db`).

## Features

- **Add Task**: Enter a new task description and add it to the list.
- **Edit Task**: Modify an existing task's description.
- **Complete Task**: Mark tasks as completed.
- **Remove Task**: Delete tasks from the list.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/AmruthaAkhila0730/to-do-list-app.git
cd to-do-list-app
```

### Install Dependencies

Install Flask and Flask-SQLAlchemy:

```bash
pip install flask flask_sqlalchemy
```

### Initialize the Database

Run the Flask application to initialize the SQLite database (`tasks.db`):

```bash
python app.py
```

This will create the necessary tables (`Task`) in the database.

## Usage

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. Open a web browser and go to [http://localhost:5000/](http://localhost:5000/) to view the application.

3. Use the application to manage your To-Do list:
   - **Add Task**: Enter a task description and click "Add Task".
   - **Edit Task**: Click "Edit" next to a task to modify its description.
   - **Complete Task**: Click "Done" to mark a task as completed.
   - **Remove Task**: Click the delete icon (`&#128465;`) to remove a task from the list.

## File Structure

```
to_do_list_app/
│
├── app.py               # Flask application script
├── models.py            # Database models (Task)
├── static/              # Static assets (CSS, JS)
│   └── style.css        # CSS styles
│
├── templates/           # HTML templates
│   ├── edit.html        # Edit task template
│   └── index.html       # Main application template
│
└── tasks.db             # SQLite database file
```

## Contributing

Contributions are welcome! Fork the repository, create a branch, make your changes, and submit a pull request. For major changes, please open an issue first to discuss potential updates.
