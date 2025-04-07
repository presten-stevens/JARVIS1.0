import unittest
import sys
import os
import datetime

# Add the parent directory of the current script to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from task_master import TaskMaster
from task import Task  # Make sure this is Task (capital 'T')

class TestTasks(unittest.TestCase):
    def setUp(self):
        """Set up a fresh TaskMaster instance before each test."""
        self.task_master = TaskMaster()

    def test_add_task(self):
        """Test adding a task."""
        print("running tests")
        self.task_master.add_task(Task("Test Task", "This is a test task", 3, "3-5-2002"))
        self.assertEqual(len(self.task_master.tasks), 1)
        self.assertEqual(self.task_master.tasks[2].title, "Test Task")
        self.assertEqual(self.task_master.tasks[2].description, "This is a test task")

    def test_delete_task(self):
        """Test deleting a task."""
        self.task_master.add_task(Task("Task to Delete", "Delete me", 3, "3-5-2002"))
        task_id = list(self.task_master.tasks.keys())[0]
        self.task_master.delete_task(task_id)
        self.assertNotIn(task_id, self.task_master.tasks)

    def test_view_tasks(self):
        """Test viewing tasks (ensuring it doesn't crash)."""
        self.task_master.add_task(Task("View Task", "This task should appear", 7, "3-5-2002"))
        self.task_master.view_tasks()  # Check output manually

    def test_task_completion(self):
        """Test marking a task as complete."""
        self.task_master.add_task(Task("Complete Task", "Finish the job", 6, "3-5-2002"))
        task_id = list(self.task_master.tasks.keys())[0]
        self.task_master.tasks[task_id].completed = True
        self.assertTrue(self.task_master.tasks[task_id].completed)
   
    def test_task_load(self):
        pass

class TestTask(unittest.TestCase):

    def setUp(self):
        # This method will run before each test
        self.task = Task(  # Fixing the lowercase `task` to `Task`
            title="Finish Homework",
            description="Complete the math homework",
            priority=2,
            due_date="2025-02-25",  # Assuming the due_date is in YYYY-MM-DD format
            category="Education"
        )

    def test_initialization(self):
        # Test the initial attributes of the task
        self.assertEqual(self.task.title, "Finish Homework")
        self.assertEqual(self.task.description, "Complete the math homework")
        self.assertEqual(self.task.priority, 2)
        self.assertEqual(self.task.category, "Education")
        self.assertFalse(self.task.completed)  # By default, completed should be False

    def test_setters(self):
        # Test the setter methods
        self.task.set_title("Complete Project")
        self.task.set_description("Finish the final project")
        self.task.set_priority(1)
        self.task.set_due_date("2025-03-01")
        self.task.set_category("Work")
        self.task.set_completed(True)

        # Check if the values were correctly updated
        self.assertEqual(self.task.title, "Complete Project")
        self.assertEqual(self.task.description, "Finish the final project")
        self.assertEqual(self.task.priority, 1)
        self.assertEqual(self.task.category, "Work")
        self.assertTrue(self.task.completed)


if __name__ == "__main__": unittest.main(verbosity=2)