import unittest
from toDoList import Task, ToDoList 


class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = ToDoList(filename="test_tasks.json")  
        self.todo_list.tasks = [] 

    def test_add_task(self):
        self.todo_list.add_task("Test Task 1", "2024-01-01", "High")
        self.assertEqual(len(self.todo_list.tasks), 1)
        self.assertEqual(self.todo_list.tasks[0].name, "Test Task 1")

    def test_edit_task(self):
        self.todo_list.add_task("Test Task 1", "2024-01-01", "High")
        self.todo_list.edit_task(1, name="Updated Task", priority="Medium")
        self.assertEqual(self.todo_list.tasks[0].name, "Updated Task")
        self.assertEqual(self.todo_list.tasks[0].priority, "Medium")

    def test_delete_task(self):
        self.todo_list.add_task("Test Task 1", "2024-01-01", "High")
        self.todo_list.add_task("Test Task 2", "2024-01-02", "Low")
        self.todo_list.delete_task(1)
        self.assertEqual(len(self.todo_list.tasks), 1)
        self.assertEqual(self.todo_list.tasks[0].name, "Test Task 2")

    def test_mark_task_as_complete(self):
        self.todo_list.add_task("Test Task 1", "2024-01-01", "High")
        self.todo_list.mark_task_as_complete(1)
        self.assertEqual(self.todo_list.tasks[0].status, "Completed")

    def test_search_tasks(self):
        self.todo_list.add_task("Shopping", "2024-01-01", "Low")
        self.todo_list.add_task("Meeting", "2024-01-02", "High")
        results = self.todo_list.search_tasks("Shop")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Shopping")

    def test_filter_tasks(self):
        self.todo_list.add_task("Task 1", "2024-01-01", "High")
        self.todo_list.add_task("Task 2", "2024-01-02", "Medium")
        self.todo_list.tasks[0].mark_as_complete()
        filtered = self.todo_list.filter_tasks(status="Completed")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].name, "Task 1")

    def tearDown(self):
        self.todo_list.tasks = []
        try:
            import os
            os.remove("test_tasks.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
