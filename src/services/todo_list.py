"""
TodoList service for core business logic of todo operations.
"""
from typing import List, Optional
from ..models.task import Task


class TodoList:
    """
    Core business logic for todo operations:
    - add_task: Creates a new Task with a unique ID and adds it to the tasks list
    - delete_task: Removes a Task from the tasks list by its ID
    - update_task: Modifies the title or description of an existing Task
    - mark_task_complete: Updates the status of a Task to complete/incomplete
    - get_all_tasks: Returns all tasks in the collection
    - get_task_by_id: Returns a specific Task by its ID or None if not found
    """
    
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id: int = 1
    
    def add_task(self, title: str, description: str = "") -> Task:
        """
        Creates a new Task with a unique ID and adds it to the tasks list.
        """
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        
        task = Task(id=self.next_id, title=title.strip(), description=description.strip())
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def delete_task(self, task_id: int) -> bool:
        """
        Removes a Task from the tasks list by its ID.
        Returns True if the task was found and deleted, False otherwise.
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False
    
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Modifies the title or description of an existing Task.
        Returns True if the task was found and updated, False otherwise.
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        if title is not None:
            title = title.strip()
            if not title:
                raise ValueError("Task title cannot be empty")
            task.title = title
        
        if description is not None:
            task.description = description.strip()
        
        return True
    
    def mark_task_complete(self, task_id: int, complete: bool = True) -> bool:
        """
        Updates the status of a Task to complete/incomplete.
        Returns True if the task was found and updated, False otherwise.
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        task.status = complete
        return True
    
    def get_all_tasks(self) -> List[Task]:
        """
        Returns all tasks in the collection.
        """
        return self.tasks.copy()
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Returns a specific Task by its ID or None if not found.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None