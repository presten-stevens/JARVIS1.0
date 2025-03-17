import tkinter as tk
from task import Task
from task_master import TaskMaster

class TaskCard(tk.Frame):
    def __init__(self, root, title, dueDate, completed, task_id):
        super().__init__(root)  # Initialize the parent Frame
        self.root = root
        self.title = title
        self.dueDate = dueDate
        self.completed = completed
        self.task_id = task_id
        self.myMaster = TaskMaster()
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
    

class CategoryContainer(tk.Frame):
    INTERIOR_PADDING = (20, 20)
    CARD_SIZE = (200, 150)
    CARD_DISPLAY_SIZE = 3
    
    def __init__(self, root, category_name: str):
        super().__init__(root)  # Initialize the parent Frame
        self.root = root
        self.name = category_name
        self.cards = []

        width = self.CARD_SIZE[0] + (2 * self.INTERIOR_PADDING[1])
        height = ((self.CARD_SIZE[1] + self.INTERIOR_PADDING[1]) * self.CARD_DISPLAY_SIZE) + 20

        self.configure(bg="grey",height=height, width=width, bd=3, relief=tk.RAISED) 
        self.grid_propagate(False)

        # title
        task_name = tk.Label(self, text=self.name, font=("Arial", 16), bg="grey")
        task_name.grid(column=0, row=0, columnspan=1, pady=5)

        self.card_frame = tk.Frame(self, bg="grey")
        self.card_frame.grid_propagate(False)
        self.card_frame.grid(row=1, column=0, sticky="nsew")
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def add_card(self, card: TaskCard):
        self.cards.append(card)
        card.grid(column=0, row=len(self.cards) - 1, pady=5, padx=5, in_=self.card_frame)
        self.update_idletasks()
    

class AddTaskButton(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        complete = tk.Button(self, width=10, text="Add Task", font=("Arial", 12), bg="green", command=self.on_click)
        complete.grid(column=0, row=0)

    def on_click(self):
        input_window = tk.Toplevel(self)
        input_window.wm_title("Add New Task")

        title = tk.StringVar()
        description = tk.StringVar()
        priority = tk.StringVar()
        due_date = tk.StringVar()
        category = tk.StringVar()

        title_label = tk.Label(input_window, text = 'Title')
        title_entry = tk.Entry(input_window, textvariable=title)

        description_label = tk.Label(input_window, text='Description')
        description_entry = tk.Entry(input_window, textvariable=description)

        priority_label = tk.Label(input_window, text='Priority')
        priority_entry = tk.Entry(input_window, textvariable=priority)

        due_date_label = tk.Label(input_window, text='Due Date')
        due_date_entry = tk.Entry(input_window, textvariable=due_date)

        category_label = tk.Label(input_window, text='Category')
        category_entry = tk.Entry(input_window, textvariable=category)

        def submit():
            task_manager.add_task(title.get(), description.get(), priority.get(), due_date.get(), category.get())
            input_window.destroy()

        submit_button = tk.Button(input_window, text = 'Submit', command=submit)

        title_label.grid(row=0,column=0)
        title_entry.grid(row=0,column=1)

        description_label.grid(row=1, column=0)
        description_entry.grid(row=1, column=1)

        priority_label.grid(row=2, column=0)
        priority_entry.grid(row=2, column=1)

        due_date_label.grid(row=3, column=0)
        due_date_entry.grid(row=3, column=1)

        category_label.grid(row=4, column=0)
        category_entry.grid(row=4, column=1)

        submit_button.grid(row=5, column=0, columnspan=2)

        

# Create main application window
root = tk.Tk()
root.title("Task Manager")


# Example Task Card (Fixed the missing arguments issue)
card = TaskCard(root, "Finish Project", "2025-03-20", False, 1)
card.grid(padx=20, pady=20)

task_manager = TaskMaster()

# Create and display Task_Card inside root
# card = TaskCard(root)
# card.grid(padx=20, pady=20)  # Ensures it appears in the window

# card2 = TaskCard(root)
# card2.grid(padx=30, pady=30) 

school = CategoryContainer(root, "School")
school.grid(row=0, column=0, padx=30, pady=30)
school.add_card(TaskCard(root, "Math Homework", "2025-03-20", False, 1))
school.add_card(TaskCard(root, "Science Project", "2025-03-20", False, 2))
school.add_card(TaskCard(root, "History Essay", "2025-03-20", False, 3))

work = CategoryContainer(root, "Work")
work.grid(row=0, column=1, padx=30, pady=30)
work.add_card(TaskCard(root, "Meeting with Boss", "2025-03-20", False, 4))
work.add_card(TaskCard(root, "Submit Report", "2025-03-20", False, 5))
work.add_card(TaskCard(root, "Prepare Presentation", "2025-03-20", False, 6))

addTask = AddTaskButton(root)
addTask.grid(padx=30, pady=30) 

root.mainloop()