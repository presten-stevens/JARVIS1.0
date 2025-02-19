import unittest
import src.task_master as master
import src.task as Task
import os
import datetime

class TestTasks(unittest.TestCase):
    def __int__(self):
        self.testMaster = master()

    def test_task_creation(self):
        # Test creating a new task
        first_line = ""
        taskName = "Go To Gym"
        self.master.add(self, taskName)
        file_path="src/save/taskA"
        self.assertFalse(os.path.exists(file_path))

    def test_task_deletion(self):
        # Test deleting a task
        self.master.delete(self, "Go To Gym")
        file_path="src/save/taskA"
        self.assertFalse(os.path.exists(file_path))

    def test_task_completion(self):
        # Test marking a task as complete
        pass
   
    def test_task_view_all(self):
        pass 

    def test_task_load(self):
        pass
        



class TestTask(unittest.TestCase):

    def setUp(self):
        # This method will run before each test
        self.task = Task(
            title="Finish Homework",
            description="Complete the math homework",
            priority=2,
            dueDate="2025-02-25",  # Assuming the dueDate is in YYYY-MM-DD format
            category="Education"
        )

    def test_initialization(self):
        # Test the initial attributes of the task
        self.assertEqual(self.task.title, "Finish Homework")
        self.assertEqual(self.task.description, "Complete the math homework")
        self.assertEqual(self.task.priority, 2)
        self.assertEqual(self.task.dueDate, datetime.strptime("2025-02-25", "%Y-%m-%d"))
        self.assertEqual(self.task.category, "Education")
        self.assertFalse(self.task.completed)  # By default, completed should be False

    def test_str_method(self):
        # Test the string representation of the task
        expected_str = (
            "Title: Finish Homework\n"
            "Description: Complete the math homework\n"
            "Priority: 2\n"
            "Due Date: 2025-02-25 00:00:00\n"  # Assuming datetime is printed this way
            "Category: Education\n"
            "Completed: False\n"
        )
        self.assertEqual(str(self.task), expected_str)

    def test_setters(self):
        # Test the setter methods
        self.task.setTitle("Complete Project")
        self.task.setDescription("Finish the final project")
        self.task.setPriority(1)
        self.task.setDueDate("2025-03-01")
        self.task.setCategory("Work")
        self.task.setCompleted(True)

        # Check if the values were correctly updated
        self.assertEqual(self.task.title, "Complete Project")
        self.assertEqual(self.task.description, "Finish the final project")
        self.assertEqual(self.task.priority, 1)
        self.assertEqual(self.task.dueDate, datetime.strptime("2025-03-01", "%Y-%m-%d"))
        self.assertEqual(self.task.category, "Work")
        self.assertTrue(self.task.completed)
