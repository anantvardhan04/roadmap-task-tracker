import argparse
import json
import os
from datetime import datetime

# File path for storing tasks
file_path = 'tasks.json'

# Get the current timestamp in a standard format
def get_timestamp():
    now = datetime.now()
    return now.strftime("%Y-%m-%dT%H:%M:%S")

# Add a task to the task list
def add_task(task):
    try:
        current_timestamp = get_timestamp()
        # Check if the file exists, create it if not
        if not os.path.exists(file_path):
            print(f"Creating {file_path} file...")
            task_item = [{
                "id": 1,
                "description": task,
                "status": "todo",
                "createdAt": current_timestamp,
                "updatedAt": current_timestamp
            }]
            with open(file_path, 'w') as task_file:
                json.dump(task_item, task_file, indent=4)
        else:
            # Read existing tasks from file
            with open(file_path, 'r') as task_file:
                data = json.load(task_file)
                # Determine the last task ID and increment it
                last_id = max(item["id"] for item in data) if data else 0
                task_item = {
                    "id": last_id + 1,
                    "description": task,
                    "status": "todo",
                    "createdAt": current_timestamp,
                    "updatedAt": current_timestamp
                }
                data.append(task_item)
            with open(file_path, 'w') as task_json:
                json.dump(data, task_json, indent=4)
        print("Task added.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Update an existing task by ID
def update_task(id, new_task):
    current_timestamp = get_timestamp()
    with open(file_path, 'r') as task_json:
        data = json.load(task_json)
    
    # Search for the task by ID and update it
    for task in data:
        if task["id"] == id:    
           task["description"] = new_task
           task["updatedAt"] = current_timestamp
           break
    
    with open(file_path,'w') as task_json:
        json.dump(data, task_json, indent=4)
    print("Task updated.")

# Delete a task by ID
def delete_task(id):
    with open(file_path, 'r') as task_json:
        data = json.load(task_json)
    
    if (list(task["id"] for task in data)).count(id) == 0:
        print(f"No task with id {id} present.")
    else:        
        for task in data:
            if task["id"] == id:
                data.remove(task)
                print("Task deleted.")
                break

    with open(file_path, 'w') as task_json:
        json.dump(data, task_json, indent=4)

# List tasks based on their status or all tasks
def list_task(filter):
    try:
        with open(file_path, 'r') as task_json:
            data = json.load(task_json)
    except FileNotFoundError:
        print("Task file not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON. Check the file content.")
        return []

    tasks_list = []
    if filter is None:
        # Return all tasks if no filter is provided
        tasks_list = [task["description"] for task in data] if data else []
    elif filter in ["todo", "in-progress", "done"]:
        # Return tasks that match the given status filter
        tasks_list = [task["description"] for task in data if task["status"] == filter]
    else:
        print("Invalid filter. Use 'todo', 'in-progress', or 'done'.")
    return tasks_list

# Update task status to in-progress or done
def update_status(id, command):
    current_timestamp = get_timestamp()
    with open(file_path, 'r') as task_json:
        data = json.load(task_json)
        
    # Update the task status based on the command
    for task in data:
        if task["id"] == id:
            if command == "mark-in-progress":
                task["status"] = "in-progress"
            elif command == "mark-done":
                task["status"] = "done"
            task["updatedAt"] = current_timestamp
            print(f"Status updated to {command}")
            break
    with open(file_path, 'w') as task_json:
        json.dump(data, task_json, indent=4)

# Main function for handling command-line arguments and invoking relevant functions
def main():
    # Create an argument parser
    parser = argparse.ArgumentParser()
    
    # Create subcommands for task management
    subparser = parser.add_subparsers(dest='command')

    # Add task subcommand
    add_parser = subparser.add_parser("add", help="Add a new task")
    add_parser.add_argument('task', type=str, help="Task description")

    # Update task subcommand
    update_parser = subparser.add_parser("update", help="Update an existing task")
    update_parser.add_argument('id', type=int, help="Task ID")
    update_parser.add_argument('task', type=str, help="New task description")
    
    # Delete task subcommand
    delete_parser = subparser.add_parser("delete", help="Delete a task by ID")
    delete_parser.add_argument('id', type=int, help="Task ID")
    
    # List tasks subcommand
    list_parser = subparser.add_parser("list", help="List tasks")
    list_parser_subparser = list_parser.add_subparsers(dest="listsubcommand")
    list_parser_subparser.add_parser("todo", help="List 'todo' tasks")
    list_parser_subparser.add_parser("in-progress", help="List 'in-progress' tasks")
    list_parser_subparser.add_parser("done", help="List 'done' tasks")
    
    # Mark task as in-progress
    mark_in_progress_parser = subparser.add_parser("mark-in-progress", help="Mark task as 'in-progress'")
    mark_in_progress_parser.add_argument("id", type=int, help="Task ID")
    
    # Mark task as done
    mark_done_parser = subparser.add_parser("mark-done", help="Mark task as 'done'")
    mark_done_parser.add_argument("id", type=int, help="Task ID")
    
    # Parse and execute the relevant subcommand
    args = parser.parse_args()
    
    if args.command == "add":
        add_task(args.task)
    elif args.command == "update":
        update_task(args.id, args.task)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "list":
        tasks = list_task(args.listsubcommand)
        if tasks:
            print("Here are your tasks:")
            for task in tasks:
                print(f"- {task}")
        else:
            print("No tasks found.")
    elif args.command in ["mark-in-progress", "mark-done"]:
        update_status(args.id, args.command)

# Entry point for the script
if __name__ == "__main__":
    main()
