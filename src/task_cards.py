import tkinter as tk
from task_master import TaskMaster as task_master

class Task_Card(tk.Frame):
    def __init__(self, root, title, dueDate, completed, task_id):
        super().__init__(root)  # Initialize the parent Frame
        self.root = root
        self.title = title
        self.dueDate = dueDate
        self.completed = completed
        self.task_id = task_id
        self.myMaster = task_master()
        # Create a frame inside Task_Card
        self.configure(bg="lightblue",height=150, width=240, padx=10, pady=10,bd=3, relief=tk.RAISED)  # Set background and padding
        # self.grid_propagate(False)
        
        # Create a label inside the frame for visibility
        self.task_name = tk.Label(self, text=self.title, font=( "Arial", 24), bg="lightblue")
        self.task_name.grid(column=0,row=0,columnspan=2)

        self.due_date = tk.Label(self, text=self.dueDate, font=( "Arial", 14), background="lightblue")
        self.due_date.grid(column=0, row=1, columnspan=2)

        self.canvas = tk.Canvas(self, width=180, height=5, highlightthickness=0, bg="lightblue")
        self.canvas.grid(column=0, row=2, columnspan=2, pady=(5, 5))

        self.canvas.create_line(10, 2, 230, 2, fill="black", width=2)

        self.complete = tk.Button(self, width=10, text="Complete", font=("Arial", 12), bg="green", command=self.on_complete_click)
        self.complete.grid(column=0, row=3, columnspan=2)
        
        self.edit = tk.Button(self, width=5, text="Edit", font=("Arial", 12), bg="blue", fg="black", command=self.on_edit_click)
        self.delete = tk.Button(self, width=5, text="Delete", font=("Arial", 12), bg="blue", command=self.on_delete_click)
        self.edit.grid(column=0, row=4)
        self.delete.grid(column=1, row=4)

    def on_complete_click(self):
        self.completed = True
        self.myMaster.editTask(self.task_id, "completed", "True")
        print("complete!!")

    def on_edit_click(self):
        """Opens a pop-up window to edit the task details."""
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Task")
        edit_window.geometry("300x200")
        edit_window.configure(bg="white")

        tk.Label(edit_window, text="Edit Task Name:", bg="white").pack(pady=5)
        name_entry = tk.Entry(edit_window)
        name_entry.insert(0, self.title)
        name_entry.pack(pady=5)

        tk.Label(edit_window, text="Edit Due Date:", bg="white").pack(pady=5)
        date_entry = tk.Entry(edit_window)
        date_entry.insert(0, self.dueDate)
        date_entry.pack(pady=5)

        def save_changes():
            new_title = name_entry.get()
            new_due_date = date_entry.get()
            if new_title and new_due_date:
                # Update internal variables
                self.title = str(new_title)
                self.dueDate = new_due_date

                # Update task in the backend
                self.myMaster.editTask(self.task_id, "title", self.title)
                self.myMaster.editTask(self.task_id, "dueDate", self.dueDate)

                # Update UI labels
                self.task_name.config(text=new_title)
                self.due_date.config(text=new_due_date)

                edit_window.destroy()
                print("Task updated!")

        save_button = tk.Button(edit_window, text="Save", bg="green", fg="white", command=save_changes)
        save_button.pack(pady=10)

        cancel_button = tk.Button(edit_window, text="Cancel", bg="red", fg="white", command=edit_window.destroy)
        cancel_button.pack(pady=5)

        print("Editing task...")

    def on_delete_click(self):
        self.myMaster.delete_task(self.task_id)
        self.destroy()
        print("delete!!")
    

# Create main application window
root = tk.Tk()
root.title("Task Manager")

# Example Task Card (Fixed the missing arguments issue)
card = Task_Card(root, "Finish Project", "2025-03-20", False, 1)
card.grid(padx=20, pady=20)

root.mainloop()