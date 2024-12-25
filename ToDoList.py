import datetime
import json

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
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["task_id"], data["name"], data["due_date"], data["priority"])
        task.status = data["status"]
        return task

    def to_string(self):
        return f"ID: {self.task_id}, Name: {self.name}, Due: {self.due_date}, Priority: {self.priority}, Status: {self.status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, due_date, priority):
        task_id = len(self.tasks) + 1
        task = Task(task_id, name, due_date, priority)
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(task.to_string())

    def edit_task(self, task_id, name=None, due_date=None, priority=None):
        for task in self.tasks:
            if task.task_id == task_id:
                task.update_task(name, due_date, priority)

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def mark_task_as_complete(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_as_complete()

    def search_tasks(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task.name.lower()]

    def filter_tasks(self, status=None, priority=None):
        filtered = self.tasks
        if status:
            filtered = [task for task in filtered if task.status == status]
        if priority:
            filtered = [task for task in filtered if task.priority == priority]
        return filtered

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            data = [task.to_dict() for task in self.tasks]
            json.dump(data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(task) for task in data]
        except FileNotFoundError:
            print("File not found. Starting with an empty to-do list.")

# Example usage
if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.load_from_file("tasks.json")
    todo_list.add_task("Complete project", "2024-12-31", "High")
    todo_list.add_task("Go jogging", "2024-12-26", "Medium")
    todo_list.view_tasks()
    print("\nSearch Results:")
    search_results = todo_list.search_tasks("project")
    for task in search_results:
        print(task.to_string())
    todo_list.save_to_file("tasks.json")
