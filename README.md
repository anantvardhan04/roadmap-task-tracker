# Task Manager Script

This Python script is a command-line utility for managing a simple task list. You can add, update, delete, list, and change the status of tasks. Tasks are stored in a `tasks.json` file.

## Features

- **Add a new task**: Add a task to the task list.
- **Update a task**: Modify an existing task by its ID.
- **Delete a task**: Remove a task by its ID.
- **List tasks**: List all tasks or filter by status (`todo`, `in-progress`, `done`).
- **Update task status**: Change the status of a task to `in-progress` or `done`.

## Installation

1. Clone the repository or download the script.
2. Make sure you have Python installed (version 3.6 or higher).
    
3. Install required dependencies (if any) using `pip`:
    
    `pip install argparse`
    
4. Make sure the script is executable by running it from your terminal.
    

## Usage

The script supports several commands for task management. All interactions are done via the command line.

### Add a New Task

To add a new task, use the `add` command followed by the task description.

`python script.py add "Buy groceries"`

### Update an Existing Task

To update an existing task's description, use the `update` command, followed by the task ID and the new description.


`python script.py update 1 "Buy groceries and cook dinner"`

### Delete a Task

To delete a task by its ID, use the `delete` command.

`python script.py delete 1`

### List Tasks

To list all tasks, use the `list` command. You can also filter tasks by status (`todo`, `in-progress`, `done`).

- List all tasks:
    
    `python script.py list`
    
- List tasks by status:
    
    `python script.py list todo` 

    `python script.py list in-progress` 
    
    `python script.py list done`
    

### Update Task Status

To mark a task as `in-progress` or `done`, use the respective command followed by the task ID.

- Mark as `in-progress`:
    
    `python script.py mark-in-progress 1`
    
- Mark as `done`:
    
    `python script.py mark-done 1`
    

## Example

Here’s an example sequence of commands:

1. Add a task:
    
    `python script.py add "Finish project report"`
    
2. List all tasks:
    
    `python script.py list`
    
3. Mark the task as `in-progress`:
    
    `python script.py mark-in-progress 1`
    
4. Update the task description:
    
    `python script.py update 1 "Finish project report and send it"`
    
5. Mark the task as `done`:
    
    `python script.py mark-done 1`
    
6. Delete the task:
    
    `python script.py delete 1`
    

## File Storage

Tasks are stored in a JSON file called `tasks.json` located in the same directory as the script. If the file does not exist, it will be created automatically when the first task is added.

## Error Handling

- If the task file is not found, you will be prompted with a message.
- If you pass an invalid filter to the `list` command, the script will notify you to use a valid filter (`todo`, `in-progress`, or `done`).
- If you try to delete or update a task that doesn’t exist, you will be informed.