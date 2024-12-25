import datetime

class Task:
    def __init__(self, task_id, name, due_date, priority):
        self.task_id = task_id
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.status = "Pending"

    def mark_as_complete(self):
        self.status = "Completed"

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

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def mark_task_as_complete(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_as_complete()

# Example usage
if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.add_task("Complete assignment", "2024-12-30", "High")
    todo_list.add_task("Grocery shopping", "2024-12-26", "Medium")
    todo_list.view_tasks()
    todo_list.mark_task_as_complete(1)
    todo_list.view_tasks()
