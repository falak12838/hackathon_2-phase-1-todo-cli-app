---

description: "Task list for Todo CLI App feature implementation"
---

# Tasks: Todo CLI App with In-Memory Storage

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in src/
- [x] T002 [P] Create models directory in src/models/
- [x] T003 [P] Create services directory in src/services/
- [x] T004 [P] Create cli directory in src/cli/
- [x] T005 [P] Create lib directory in src/lib/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 [P] Create Task data model in src/models/task.py (based on data-model.md)
- [x] T007 [P] Create TodoList service in src/services/todo_list.py (based on data-model.md)
- [x] T008 Create utils module in src/lib/utils.py for helper functions
- [x] T009 Configure error handling infrastructure in src/lib/utils.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Implement the ability to add new tasks with title and description to the todo list

**Independent Test**: The user can run the command to add a task with a title and description, and the system will confirm the task has been added with a unique ID.

### Implementation for User Story 1

- [x] T010 [P] [US1] Implement Task data model with required attributes in src/models/task.py
- [x] T011 [P] [US1] Implement TodoList.add_task method in src/services/todo_list.py
- [x] T012 [US1] Implement CLI menu option for adding tasks in src/cli/main.py
- [x] T013 [US1] Add input validation for task title in src/lib/utils.py
- [x] T014 [US1] Add unique ID assignment logic in src/services/todo_list.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Implement the ability to view all tasks with their ID, title, description, and completion status

**Independent Test**: The user can run the command to view all tasks, and the system will display a formatted list of all tasks with their details.

### Implementation for User Story 2

- [x] T015 [P] [US2] Implement TodoList.get_all_tasks method in src/services/todo_list.py
- [x] T016 [US2] Implement formatted output display in src/cli/main.py
- [x] T017 [US2] Add visual status indicators ([ ] for incomplete, [x] for complete) in src/cli/main.py
- [x] T018 [US2] Implement CLI menu option for viewing tasks in src/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Task as Complete (Priority: P2)

**Goal**: Implement the ability to mark tasks as complete using their ID

**Independent Test**: The user can run the command to mark a specific task as complete using its ID, and the system will update the task's status.

### Implementation for User Story 3

- [x] T019 [P] [US3] Implement TodoList.mark_task_complete method in src/services/todo_list.py
- [x] T020 [P] [US3] Implement TodoList.get_task_by_id method in src/services/todo_list.py
- [x] T021 [US3] Implement CLI menu option for marking tasks as complete in src/cli/main.py
- [x] T022 [US3] Add error handling for invalid task IDs in src/lib/utils.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task Details (Priority: P2)

**Goal**: Implement the ability to update the title or description of an existing task using its ID

**Independent Test**: The user can run the command to update a specific task's title or description using its ID, and the system will update the task details.

### Implementation for User Story 4

- [x] T023 [P] [US4] Implement TodoList.update_task method in src/services/todo_list.py
- [x] T024 [US4] Implement CLI menu option for updating tasks in src/cli/main.py
- [x] T025 [US4] Add validation for updated task title in src/lib/utils.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Task (Priority: P3)

**Goal**: Implement the ability to delete tasks from the todo list using their ID

**Independent Test**: The user can run the command to delete a specific task using its ID, and the system will remove the task from the list.

### Implementation for User Story 5

- [x] T026 [P] [US5] Implement TodoList.delete_task method in src/services/todo_list.py
- [x] T027 [US5] Implement CLI menu option for deleting tasks in src/cli/main.py
- [x] T028 [US5] Add confirmation prompt for task deletion in src/cli/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T029 [P] Add comprehensive error handling throughout the application
- [x] T030 [P] Add type hints to all functions and methods
- [x] T031 [P] Add docstrings to all public functions and classes
- [x] T032 Implement main application loop in src/cli/main.py
- [x] T033 Add help documentation accessible via a help command in src/cli/main.py
- [x] T034 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Models before services
- Services before CLI interface
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all models for User Story 1 together:
Task: "Implement Task data model with required attributes in src/models/task.py"
Task: "Implement TodoList.add_task method in src/services/todo_list.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence