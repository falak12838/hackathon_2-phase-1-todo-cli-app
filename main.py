"""
CLI interface and main application loop for the todo CLI application.
"""
from typing import Optional
import sys
import os

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from src.services.todo_list import TodoList
from src.lib.utils import validate_task_title, get_valid_task_id


class TodoCLI:
    """
    Command-line interface for the todo application.
    """
    
    def __init__(self):
        self.todo_list = TodoList()
    
    def display_menu(self):
        """
        Display the main menu options.
        """
        print("\n=== Todo CLI Application ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Complete")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Help")
        print("7. Exit")
        print("============================")
    
    def add_task(self):
        """
        Add a new task to the todo list.
        """
        try:
            title = input("Enter task title: ").strip()
            description = input("Enter task description (optional): ").strip()
            
            # Validate the title
            validate_task_title(title)
            
            task = self.todo_list.add_task(title, description)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def view_tasks(self):
        """
        Display all tasks in the todo list.
        """
        tasks = self.todo_list.get_all_tasks()
        
        if not tasks:
            print("No tasks in the list.")
            return
        
        print("\nID  | Status | Title                 | Description")
        print("----|--------|-----------------------|------------")
        for task in tasks:
            status = "[x]" if task.status else "[ ]"
            title = task.title[:19] + "..." if len(task.title) > 19 else task.title
            description = task.description[:19] + "..." if len(task.description) > 19 else task.description
            print(f"{task.id:<3} | {status:<6} | {title:<21} | {description}")
    
    def mark_task_complete(self):
        """
        Mark a task as complete or incomplete.
        """
        try:
            task_id_str = input("Enter task ID to mark as complete: ").strip()
            task_id = get_valid_task_id(task_id_str)
            
            if self.todo_list.mark_task_complete(task_id):
                print(f"Task {task_id} marked as complete.")
            else:
                print(f"Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def update_task(self):
        """
        Update the title or description of an existing task.
        """
        try:
            task_id_str = input("Enter task ID to update: ").strip()
            task_id = get_valid_task_id(task_id_str)
            
            # Check if task exists
            task = self.todo_list.get_task_by_id(task_id)
            if not task:
                print(f"Task with ID {task_id} not found.")
                return
            
            print(f"Current title: {task.title}")
            new_title = input("Enter new title (or press Enter to keep current): ").strip()
            
            print(f"Current description: {task.description}")
            new_description = input("Enter new description (or press Enter to keep current): ").strip()
            
            # Update title if provided
            if new_title:
                validate_task_title(new_title)
                title_to_update = new_title
            else:
                title_to_update = None
            
            # Update description if provided
            if new_description:
                description_to_update = new_description
            else:
                description_to_update = None
            
            if self.todo_list.update_task(task_id, title_to_update, description_to_update):
                print(f"Task {task_id} updated successfully.")
            else:
                print(f"Failed to update task {task_id}.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def delete_task(self):
        """
        Delete a task from the todo list.
        """
        try:
            task_id_str = input("Enter task ID to delete: ").strip()
            task_id = get_valid_task_id(task_id_str)
            
            if self.todo_list.delete_task(task_id):
                print(f"Task {task_id} deleted successfully.")
            else:
                print(f"Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def show_help(self):
        """
        Display help information.
        """
        print("\n=== Help ===")
        print("1. Add Task: Create a new task with a title and optional description")
        print("2. View All Tasks: Display all tasks with their ID, status, title, and description")
        print("3. Mark Task as Complete: Change the status of a task to complete")
        print("4. Update Task: Modify the title or description of an existing task")
        print("5. Delete Task: Remove a task from the list")
        print("6. Help: Show this help message")
        print("7. Exit: Quit the application")
        print("============")
    
    def run(self):
        """
        Main application loop.
        """
        print("Welcome to the Todo CLI Application!")
        
        while True:
            self.display_menu()
            choice = input("Select an option (1-7): ").strip()
            
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.mark_task_complete()
            elif choice == '4':
                self.update_task()
            elif choice == '5':
                self.delete_task()
            elif choice == '6':
                self.show_help()
            elif choice == '7':
                print("Thank you for using the Todo CLI Application. Goodbye!")
                break
            else:
                print("Invalid option. Please select a number between 1 and 7.")


if __name__ == "__main__":
    cli = TodoCLI()
    cli.run()