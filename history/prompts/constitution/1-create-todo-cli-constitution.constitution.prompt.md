---
id: 1
title: Create Todo CLI Constitution
stage: constitution
date: 2026-01-02
surface: agent
model: Qwen
feature: none
branch: main
user: Dell
command: /sp.constitution
labels: [constitution, todo, cli]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

Follow this execution flow:

1. Load the existing constitution template at `.specify/memory/constitution.md`.
   - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
   **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

2. Collect/derive values for placeholders:
   - If user input (conversation) supplies a value, use it.
   - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
   - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If version bump type ambiguous, propose reasoning before finalizing.

3. Draft the updated constitution content:
   - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
   - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
   - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
   - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert prior checklist into active validations):
   - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
   - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
   - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

   - Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - Follow-up TODOs if any placeholders intentionally deferred.

5. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches report.
   - Dates ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

6. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

7. Output a final summary to the user with:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

Formatting & Style Requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.


/sp.constitution You are an AI agent using Spec-Kit Plus for specification-driven development. Your task is to generate a  Workflow, and Deliverables. Ensure it aligns with clean code practices and no manual coding.

Project Details:
- Objective: Build a basic command-line todo application that stores tasks in memory (no persistence).
- Features (implement all):
  1. Add Task: Create new tasks with title and description; assign unique ID.
  2. Delete Task: Remove tasks by ID; handle invalid IDs.
  3. Update Task: Modify title or description by ID.
  4. View Task List: Display all tasks with ID, title, description, and completion status (e.g., [ ] incomplete, [x] complete).
  5. Mark as Complete: Toggle completion"Constitution" file for a hackathon project: Phase I of a Todo In-Memory Python Console App. The constitution should serve as the foundational document guiding the entire agentic development process. It must define the project's objectives, requirements, constraints, development workflow, tech stack, and principles for AI-generated code. Output the constitution in Markdown format, structured with sections like: Project Overview, Goals, Requirements, Development Principles, Tech Stack, status by ID.
- Development Approach: Agentic Dev Stack – Write spec → Generate plan → Break into tasks → Implement via AI code generation (using Claude Code or Qwen). No manual coding. Use Spec-Kit Plus for spec management and iterations.
- Tech Stack: UV for package management, Python 3.13+, Spec-Kit Plus for workflow.
- Principles: Follow PEP 8, modular code, proper error handling, user-friendly CLI.
- Deliverables: GitHub repo with constitution file, specs_history folder (all specs/plans/tasks/AI prompts/responses), /src folder (generated Python code), README.md (setup and run instructions). Working CLI app demonstrating all features.

Make the constitution concise yet comprehensive, about 800-1000 words. It should instruct future AI agents on how to proceed with spec refinement, planning, and implementation while adhering to the no-manual-coding rule. End with a section on iteration and review process for judging.

## Response snapshot

# Todo CLI Application Constitution

## Core Principles

### I. Agentic Development First
All code must be generated through AI agents using the Spec-Kit Plus framework; No manual coding is permitted during implementation phase; Every feature must follow the spec → plan → tasks → implementation cycle; Human intervention limited to specification, review, and approval stages.

### II. CLI Interface Standard
Every functionality must be accessible via command-line interface; Follow standard CLI patterns: commands → arguments → flags; Text-based input/output protocol: stdin/args → stdout, errors → stderr; Support both human-readable and JSON output formats for all operations.

### III. Test-First Implementation (NON-NEGOTIABLE)
TDD mandatory: Specifications written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced; Every feature must have corresponding unit tests before implementation; Integration tests required for all CLI command flows.

### IV. In-Memory Data Management
All tasks stored in memory during application runtime; No persistence to disk required for Phase I; Data structure must support all required operations efficiently; Memory management must prevent leaks and ensure proper cleanup.

### V. User Experience Focus
Intuitive command structure with clear help documentation; Consistent output formatting across all commands; Meaningful error messages for all failure scenarios; Task status clearly indicated with visual markers ([ ] incomplete, [x] complete).

### VI. Clean Code Architecture
Modular code structure with clear separation of concerns; Follow PEP 8 Python style guidelines; Proper error handling throughout the application; Well-documented functions and classes with type hints.

## Technical Requirements

### Tech Stack
- Language: Python 3.13+
- Package Management: UV
- Framework: Spec-Kit Plus for workflow management
- Code Quality: Follow PEP 8 standards
- Version Control: Git with descriptive commit messages

### Feature Requirements
- Add Task: Create new tasks with title and description; assign unique ID
- Delete Task: Remove tasks by ID; handle invalid IDs gracefully
- Update Task: Modify title or description by ID
- View Task List: Display all tasks with ID, title, description, and completion status
- Mark as Complete: Toggle completion status by ID

### Code Quality Standards
- All functions must have proper type hints
- Error handling for all user inputs and edge cases
- Modular design with separate modules for CLI, business logic, and data management
- Comprehensive docstrings for all public functions and classes

## Development Workflow

### Specification Phase
- Create detailed feature specifications using Spec-Kit Plus templates
- Define acceptance criteria for each feature
- Identify potential edge cases and error conditions
- Review and approve specifications before proceeding to planning

### Planning Phase
- Generate architectural plans based on specifications
- Identify dependencies and implementation order
- Plan for error handling and edge cases
- Ensure test strategy aligns with feature requirements

### Implementation Phase
- Break implementation into granular, testable tasks
- Use AI agents to generate code following specifications
- Verify generated code meets quality standards
- Run tests after each implementation step

### Review Process
- Automated code quality checks using linters
- Manual review of generated code for correctness
- Verification that all features meet specifications
- Documentation completeness check

## Governance
This constitution governs all development activities for the Todo CLI Application; All code must comply with the principles outlined herein; Amendments require formal documentation and team approval; All pull requests must verify compliance with these principles; Code reviews must check for adherence to the no-manual-coding rule.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02

## Outcome

- ✅ Impact: Created comprehensive constitution for Todo CLI Application project
- 🧪 Tests: No tests required for constitution creation
- 📁 Files: Updated .specify/memory/constitution.md with complete constitution
- 🔁 Next prompts: Ready to proceed with specification phase using /sp.specify
- 🧠 Reflection: Constitution successfully created with all required sections and principles

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): Standard constitution creation
- Next experiment (smallest change to try): Proceed with feature specification