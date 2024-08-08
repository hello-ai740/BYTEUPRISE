
import os

TASKS = 'task.txt'

def load_tasks():
    if not os.path.exists(TASKS):
        return []
    with open(TASKS, 'r') as file:
        return file.read().splitlines()

def save_tasks(tasks):
    with open(TASKS, 'w') as file:
        file.write('\n'.join(tasks))

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def delete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        delete_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{delete_task}' deleted.")
    else:
        print("Invalid task index.")

def updated_tasks():
    tasks = load_tasks()
    if tasks:
        print("Your tasks:")
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")


def list():
    while True:
        print("\n*****To-Do-List*****")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Updated Tasks")
        print("4. Stop")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            task = input("Enter the task you want to add: ")
            add_task(task)
        elif choice == '2':
            updated_tasks()
            try:
                task_index = int(input("Enter the task number to delete: "))
                delete_task(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            updated_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")

if __name__ == '__main__':
   list()           

