# AGENTS.md — BrewOS

## 1. Project Overview

BrewOS is a Python-based desktop application built using CustomTkinter.

The application follows a modular architecture with separate UI components, page managers, reusable utilities, theme management and application logic.

The primary development goals are:
- Maintainable and modular code.
- Consistent UI and application behaviour.
- Reusable components and utilities.
- Clean separation of responsibilities.
- A cohesive and polished desktop experience.

## 2. General Development Principles

- Always inspect the existing implementation before making changes.
- Follow the established project architecture and coding conventions.
- Prefer extending existing implementations over introducing duplicate functionality.
- Avoid unnecessary abstractions, dependencies and complexity.
- Keep implementations modular and responsibilities clearly separated.
- Prioritise readability, maintainability and reliability over clever or overly compact solutions.
- Do not redesign or restructure unrelated parts of the application.

## 3. UI Development

BrewOS uses CustomTkinter for its graphical interface.

- Use CustomTkinter for new UI components unless an existing implementation requires otherwise.
- Maintain consistency with the existing UI design and component structure.
- Reuse existing frames, widgets, managers and utilities wherever possible.
- Follow the positioning and layout approach used by the relevant parent component.
- Respect the dimensions and boundaries of parent frames.
- Avoid hardcoding colours when an equivalent theme value exists.
- Avoid unnecessary widget recreation and duplicated UI logic.
- Keep UI components separate from application and data-handling logic.

### Page Architecture

- Inspect existing page implementations before creating new pages.
- Follow the existing inheritance, constructor and initialization conventions.
- Reuse the established page-management and navigation mechanisms.
- Respect the existing page lifecycle and animation patterns.
- Do not introduce a new navigation or page-management system without explicit approval.
- Ensure new pages integrate with their intended parent frames correctly.

## 4. Theme and Icon Management

BrewOS uses dedicated ThemeManager and IconManager classes.

- Use ThemeManager to retrieve theme colours and appearance-related values.
- Use IconManager for existing application icons.
- Do not introduce independent colour palettes or duplicate icon-loading mechanisms.
- Avoid hardcoded colours when corresponding theme entries are available.
- Preserve compatibility with the existing theme-switching mechanism.
- Do not modify theme definitions or icon management unnecessarily.

## 5. Python Coding Standards

- Follow PEP 8 where practical and remain consistent with existing code.
- Use meaningful variable, function and class names.
- Use type annotations where they improve clarity.
- Keep functions and methods focused on a single responsibility.
- Avoid unnecessary global variables.
- Avoid circular imports.
- Handle exceptions appropriately.
- Use pathlib where appropriate for filesystem operations.
- Avoid unnecessary dependencies and third-party packages.

## 6. Project Structure

- Preserve the existing directory organisation.
- Place new modules in the appropriate existing package.
- Follow existing naming conventions.
- Keep related functionality together.
- Avoid creating additional directories or modules unless they serve a clear purpose.
- Do not rename or move existing files without explicit approval.

## 7. Change Management

Before implementing a task:

1. Inspect the relevant modules and their dependencies.
2. Understand how the existing implementation works.
3. Identify the files that need modification.
4. Consider possible side effects and compatibility issues.

During implementation:

- Modify only files relevant to the requested task.
- Preserve existing functionality unless explicitly asked to change it.
- Do not overwrite unrelated user modifications.
- Do not silently remove existing functionality.
- Ask for approval before making substantial architectural changes.
- Ask before modifying files outside the requested scope when they are not clearly necessary.

After implementation:

- Summarise the changes made.
- List created and modified files.
- Explain important implementation decisions.
- Mention potential side effects or remaining limitations.

## 8. Testing and Verification

- Inspect the available project configuration before running commands.
- Use the project's existing Python environment and dependencies.
- Verify imports and module compatibility.
- Run relevant tests when available.
- Perform appropriate static checks when automated tests are unavailable.
- Verify application initialization when changes affect startup or UI integration.
- Do not claim something was tested unless it was actually tested.
- Clearly distinguish verified behaviour from assumptions.

## 9. Git Guidelines

- Do not commit, push, reset, rebase or amend commits unless explicitly requested.
- Never discard or overwrite existing user changes.
- Inspect the working tree before substantial modifications.
- Do not modify Git configuration unnecessarily.
- Preserve existing commit history and branch structure.

## 10. Communication and Collaboration

- Explain important implementation decisions rather than simply presenting generated code.
- When asked to teach, explain unfamiliar Python concepts and design patterns.
- Prefer direct, technically accurate explanations.
- Identify architectural trade-offs instead of presenting every implementation as universally correct.
- Ask for clarification when requirements are genuinely ambiguous.
- Do not make assumptions about functionality that has not been established in the codebase.

## 11. Instruction Priority

Follow the user's explicit task requirements first, provided they do not conflict with higher-priority instructions.

These project guidelines establish defaults, not permission to make unrelated changes.

When uncertain about an architectural decision, inspect existing implementations and ask before introducing a substantially different approach.