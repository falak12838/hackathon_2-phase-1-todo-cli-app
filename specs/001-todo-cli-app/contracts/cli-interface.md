# Contract: Todo CLI Interface

## CLI Commands Interface

### Add Task
- **Command**: Option 1 from main menu
- **Input**: Title (required), Description (optional)
- **Output**: Confirmation message with assigned ID
- **Error Cases**: Empty title results in error message

### View Tasks
- **Command**: Option 2 from main menu
- **Input**: None
- **Output**: Formatted list of all tasks with ID, status indicator, title, and description
- **Error Cases**: No tasks message when list is empty

### Mark Task Complete
- **Command**: Option 3 from main menu
- **Input**: Task ID
- **Output**: Confirmation message of status change
- **Error Cases**: Invalid ID results in error message

### Update Task
- **Command**: Option 4 from main menu
- **Input**: Task ID, new title (optional), new description (optional)
- **Output**: Confirmation message of update
- **Error Cases**: Invalid ID or empty title results in error message

### Delete Task
- **Command**: Option 5 from main menu
- **Input**: Task ID
- **Output**: Confirmation message of deletion
- **Error Cases**: Invalid ID results in error message

### Exit
- **Command**: Option 6 from main menu
- **Input**: None
- **Output**: Application termination

## Data Contracts

### Task Object
```
{
  "id": int,
  "title": str,
  "description": str,
  "status": bool
}
```

### CLI Output Format
```
ID  Status  Title           Description
--  ------  -----           -----------
1   [ ]     Sample Task     Description of the task
2   [x]     Completed Task  Another description
```