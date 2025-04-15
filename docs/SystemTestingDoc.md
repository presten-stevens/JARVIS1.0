Test cases for functional, non-functional, and regression testing.

Results and observations.

Updated unit and integration tests to reflect all features.


# Functional

- Tested editing task in both uncompleted and completed states. Changes on the frontend reflect on the backend.
- Adding a task and then checking the calendar doesn't update on the calendar. Tags alos don't update after creation.
- When editing a task, the current information does not show up in the input fields.
- Completing a task and saving will load the task in the completed category.

# Non-functional

- Deleting a task deletes the JSON, therefore it can't be loaded again.
- After deleting a task the deleted ID is not used again.

# Regression testing

- Calendar view properly displays tasks at proper times.
- Having multiple tasks on the calendar properly list and don't overlap