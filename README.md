# Todo CLI Application

A simple command-line todo application with in-memory storage that allows users to add, view, update, delete, and mark tasks as complete.

## Features

- Add new tasks with title and description
- View all tasks with ID, status, title, and description
- Mark tasks as complete/incomplete
- Update task title or description
- Delete tasks
- Help documentation

## Requirements

- Python 3.13+

## Installation

1. Clone or download this repository
2. Navigate to the project directory

## Usage

Run the application using Python:

```bash
python -m src.cli.main
```

## Functionality

Once the application is running, you'll see a menu with the following options:

1. **Add Task**: Create a new task with a title and optional description
2. **View All Tasks**: Display all tasks with their ID, status, title, and description
3. **Mark Task as Complete**: Change the status of a task to complete
4. **Update Task**: Modify the title or description of an existing task
5. **Delete Task**: Remove a task from the list
6. **Help**: Show help information
7. **Exit**: Quit the application

## Example Workflow

1. Launch the application: `python -m src.cli.main`
2. Select option 1 to add a new task
3. Enter a title and optional description
4. Select option 2 to view all tasks
5. Select option 3 to mark a task as complete
6. Select option 4 to update a task
7. Select option 5 to delete a task
8. Select option 7 to exit the application

## Architecture

The application follows a modular architecture:

- `src/models/task.py`: Defines the Task data model
- `src/services/todo_list.py`: Contains the business logic for todo operations
- `src/cli/main.py`: Implements the command-line interface
- `src/lib/utils.py`: Provides utility functions

## License

This project is open source and available under the MIT License.