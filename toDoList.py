import json
import os


class Task:
    def __init__(self, task_id, name, due_date, priority):
        self.task_id = task_id
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.status = "Pending"

    def mark_as_complete(self):
        self.status = "Completed"

    def update_task(self, name=None, due_date=None, priority=None):
        if name:
            self.name = name
        if due_date:
            self.due_date = due_date
        if priority:
            self.priority = priority

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "name": self.name,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["task_id"], data["name"], data["due_date"], data["priority"])
        task.status = data["status"]
        return task

    def to_string(self):
        return f"ID: {self.task_id}, Name: {self.name}, Due: {self.due_date}, Priority: {self.priority}, Status: {self.status}"


class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_from_file()

    def add_task(self, name, due_date, priority):
        task_id = len(self.tasks) + 1
        task = Task(task_id, name, due_date, priority)
        self.tasks.append(task)
        print(f"Task '{name}' added successfully!")
        self.save_to_file()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            print("\n--- To-Do List ---")
            for task in self.tasks:
                print(task.to_string())
            print("------------------")

    def edit_task(self, task_id, name=None, due_date=None, priority=None):
        for task in self.tasks:
            if task.task_id == task_id:
                task.update_task(name, due_date, priority)
                print(f"Task ID {task_id} updated successfully!")
                self.save_to_file()
                return
        print(f"No task found with ID {task_id}.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"Task ID {task_id} deleted successfully!")
                self.save_to_file()
                return
        print(f"No task found with ID {task_id}.")

    def mark_task_as_complete(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_as_complete()
                print(f"Task ID {task_id} marked as complete!")
                self.save_to_file()
                return
        print(f"No task found with ID {task_id}.")

    def search_tasks(self, keyword):
        results = [task for task in self.tasks if keyword.lower() in task.name.lower()]
        if results:
            print("\n--- Search Results ---")
            for task in results:
                print(task.to_string())
            print("----------------------")
        else:
            print("No tasks found matching the keyword.")

    def filter_tasks(self, status=None, priority=None):
        filtered = self.tasks
        if status:
            filtered = [task for task in filtered if task.status == status]
        if priority:
            filtered = [task for task in filtered if task.priority == priority]

        if filtered:
            print("\n--- Filtered Tasks ---")
            for task in filtered:
                print(task.to_string())
            print("----------------------")
        else:
            print("No tasks found matching the filter.")

    def save_to_file(self):
        with open(self.filename, "w") as file:
            data = [task.to_dict() for task in self.tasks]
            json.dump(data, file)

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(task) for task in data]
        else:
            self.tasks = []


def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Search Tasks")
        print("7. Filter Tasks")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            name = input("Enter task name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (High/Medium/Low): ")
            todo_list.add_task(name, due_date, priority)

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID to edit: "))
            name = input("Enter new task name (or press Enter to skip): ")
            due_date = input("Enter new due date (or press Enter to skip): ")
            priority = input("Enter new priority (or press Enter to skip): ")
            todo_list.edit_task(task_id, name if name else None, due_date if due_date else None, priority if priority else None)

        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)

        elif choice == "5":
            task_id = int(input("Enter task ID to mark as complete: "))
            todo_list.mark_task_as_complete(task_id)

        elif choice == "6":
            keyword = input("Enter keyword to search: ")
            todo_list.search_tasks(keyword)

        elif choice == "7":
            print("\n--- Filter Options ---")
            status = input("Enter status to filter (Pending/Completed or press Enter to skip): ")
            priority = input("Enter priority to filter (High/Medium/Low or press Enter to skip): ")
            todo_list.filter_tasks(status if status else None, priority if priority else None)

        elif choice == "8":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
