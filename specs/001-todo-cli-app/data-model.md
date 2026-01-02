# Data Model: Todo CLI App

## Task Entity

### Attributes
- **id**: `int` - Unique identifier assigned when the task is created (auto-incrementing)
- **title**: `str` - Required string representing the task name (non-empty)
- **description**: `str` - Optional string providing additional details about the task (can be empty)
- **status**: `bool` - Boolean indicating whether the task is complete (True) or incomplete (False), default False

### Validation Rules
- ID must be a positive integer
- Title must be a non-empty string (length > 0)
- Description can be an empty string
- Status must be a boolean value

### State Transitions
- Status can transition from `False` (incomplete) to `True` (complete) when marked as complete
- Status can transition from `True` (complete) to `False` (incomplete) when marked as incomplete

## TodoList Entity

### Attributes
- **tasks**: `List[Task]` - Collection of Task objects stored in memory
- **next_id**: `int` - Counter for generating unique IDs for new tasks, starts at 1

### Operations
- **add_task(title: str, description: str = "")**: Creates a new Task with a unique ID and adds it to the tasks list
- **delete_task(task_id: int)**: Removes a Task from the tasks list by its ID
- **update_task(task_id: int, title: str = None, description: str = None)**: Modifies the title or description of an existing Task
- **mark_task_complete(task_id: int, complete: bool = True)**: Updates the status of a Task to complete/incomplete
- **get_all_tasks()**: Returns all tasks in the collection
- **get_task_by_id(task_id: int)**: Returns a specific Task by its ID or None if not found

### Validation Rules
- Task IDs must be unique within the collection
- Operations targeting a specific task ID must verify the task exists before performing the operation
- Title updates must not result in an empty string