"""
Task data model representing a single todo item.
"""
from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents a single todo item with the following attributes:
    - id: A unique identifier assigned when the task is created
    - title: A required string representing the task name
    - description: An optional string providing additional details about the task
    - status: A boolean indicating whether the task is complete (true) or incomplete (false)
    """
    id: int
    title: str
    description: str = ""
    status: bool = False