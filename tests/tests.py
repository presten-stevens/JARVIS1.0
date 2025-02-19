import unittest
import sys
import os
import datetime

# Add the parent directory of the current script to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.task_master import TaskMaster as master
from src.task import task  # Make sure this is Task (capital 'T')

class TestTasks(unittest.TestCase):
    def setUp(self):
        """Set up a fresh TaskMaster instance before each test."""
        self.task_master = master.task_master()

    def test_add_task(self):
        """Test adding a task."""
        print("running tests")
        self.task_master.add_task("Test Task", "This is a test task")
        self.assertEqual(len(self.task_master.tasks), 1)
        self.assertEqual(self.task_master.tasks[1].name, "Test Task")
        self.assertEqual(self.task_master.tasks[1].description, "This is a test task")

    def test_delete_task(self):
        """Test deleting a task."""
        self.task_master.add_task("Task to Delete", "Delete me")
        task_id = list(self.task_master.tasks.keys())[0]
        self.task_master.delete_task(task_id)
        self.assertNotIn(task_id, self.task_master.tasks)

    def test_view_tasks(self):
        """Test viewing tasks (ensuring it doesn't crash)."""
        self.task_master.add_task("View Task", "This task should appear")
        self.task_master.view_tasks()  # Check output manually

    def test_task_completion(self):
        """Test marking a task as complete."""
        self.task_master.add_task("Complete Task", "Finish the job")
        task_id = list(self.task_master.tasks.keys())[0]
        self.task_master.tasks[task_id].completed = True
        self.assertTrue(self.task_master.tasks[task_id].completed)
   
    def test_task_load(self):
        pass

class TestTask(unittest.TestCase):

    def setUp(self):
        # This method will run before each test
        self.task = task(  # Fixing the lowercase `task` to `Task`
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
        self.assertEqual(self.task.dueDate, datetime.datetime.strptime("2025-02-25", "%Y-%m-%d"))  # Fixing the datetime import
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
        self.assertEqual(self.task.dueDate, datetime.datetime.strptime("2025-03-01", "%Y-%m-%d"))
        self.assertEqual(self.task.category, "Work")
        self.assertTrue(self.task.completed)


if __name__ == "__main__": unittest.main(verbosity=2)