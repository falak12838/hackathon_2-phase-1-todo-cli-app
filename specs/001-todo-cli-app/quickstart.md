# Quickstart Guide: Todo CLI App

## Prerequisites
- Python 3.13+ installed
- UV package manager (optional, for dependency management)

## Setup
1. Clone or create the project directory
2. Create the following directory structure:
```
src/
├── models/
│   └── task.py
├── services/
│   └── todo_list.py
├── cli/
│   └── main.py
└── lib/
    └── utils.py
```

## Running the Application
1. Navigate to the project root directory
2. Run the application: `python -m src.cli.main`
3. The application will display a menu with options to add, view, update, delete, and mark tasks as complete

## Basic Usage
1. Launch the application
2. Select options from the menu by entering the corresponding number
3. Follow the prompts to provide required information
4. Use option 6 to exit the application

## Example Workflow
1. Add a new task: Select option 1, enter title and description
2. View all tasks: Select option 2 to see your task list
3. Mark a task as complete: Select option 3, enter the task ID
4. Update a task: Select option 4, enter the task ID and new details
5. Delete a task: Select option 5, enter the task ID
6. Exit: Select option 6 to quit the application

## Error Handling
- Invalid menu selections will prompt you to try again
- Invalid task IDs will display an appropriate error message
- Empty titles will be rejected when adding or updating tasks