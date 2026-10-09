# Task Tracker CLI

A simple command-line task management application built with Python.

This project is based on the [Task Tracker project](https://roadmap.sh/projects/task-tracker) from roadmap.sh.

## Features

* Add new tasks
* Update task descriptions
* Delete tasks by ID
* Mark tasks as `todo`, `in progress`, or `done`
* List all tasks
* Filter tasks by status
* Automatically track creation and update dates
* Save and load tasks using JSON

## Technologies

* Python
* argparse
* JSON
* datetime
* Object-Oriented Programming (OOP)

No external dependencies are required.

## Installation

Clone the repository and run:

```bash
python task_tracker.py
```

## Usage

The application supports the following commands:

### Add a task

```bash
add "Buy groceries"
```

### Update a task

```bash
update 1 "Buy groceries and cook dinner"
```

### Delete a task

```bash
delete 1
```

### Update task status

```bash
mark-in-progress 1
mark-done 1
```

### List tasks

```bash
list
list todo
list in-progress
list done
```

### Exit

```bash
quit
```

## Data Storage

Tasks are stored locally in `tasks.json`.

Example:

```json
[
    {
        "id": 1,
        "description": "Learn Python",
        "status": "done",
        "createdAt": "2026-10-01",
        "updatedAt": "2026-10-05"
    },
    {
        "id": 2,
        "description": "Build Task Tracker CLI",
        "status": "in progress",
        "createdAt": "2026-10-09",
        "updatedAt": "2026-10-09"
    }
]
```

Each task contains a unique ID, description, status, creation date, and last update date.

## Project Structure

```text
task-tracker/
├── task_tracker.py
├── tasks.json
└── README.md
```

## Project Goal

This project was created to practice Python programming, object-oriented design, command-line argument parsing, file handling, and JSON serialization.
