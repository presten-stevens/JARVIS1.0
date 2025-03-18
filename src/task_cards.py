import tkinter as tk
from task import Task
from task_master import TaskMaster

task_manager = TaskMaster()

class TaskCard(tk.Frame):
    def __init__(self, root, task: Task):
        super().__init__(root)  # Initialize the parent Frame
        self.root = root
        self.id = task_manager.add_task(task.title, task.description, task.priority, task.due_date, task.category, task.completed)
        self.update_task()

        # Create a frame inside Task_Card
        self.configure(bg="lightblue",height=150, width=240, padx=10, pady=10,bd=3, relief=tk.RAISED)  # Set background and padding
        
        # Create a label inside the frame for visibility
        self.task_name = tk.Label(self, text=self.task.title, font=( "Arial", 24), bg="lightblue")  
        self.task_name.grid(column=0,row=0,columnspan=2)

        self.due_date = tk.Label(self, text=self.task.due_date, font=( "Arial", 14), background="lightblue")
        self.due_date.grid(column=0, row=1, columnspan=2)

        self.canvas = tk.Canvas(self, width=180, height=5, highlightthickness=0, bg="lightblue")
        self.canvas.grid(column=0, row=2, columnspan=2, pady=(5, 5))

        self.canvas.create_line(10, 2, 230, 2, fill="black", width=2)

        self.complete = tk.Button(self, width=10, text="Complete", font=("Arial", 12), bg="green", command=self.on_complete_click)
        self.complete.grid(column=0, row=3, columnspan=2)
        
        self.edit = tk.Button(self, width=5, text="Edit", font=("Arial", 12), bg="azure4", fg="black", command=self.on_edit_click)
        self.delete = tk.Button(self, width=5, text="Delete", font=("Arial", 12), bg="azure4", command=self.on_delete_click)
        self.edit.grid(column=0, row=4)
        self.delete.grid(column=1, row=4)

    def update_task(self):
        self.task = task_manager.get_task(self.id)

    def on_complete_click(self):
        if self.task.completed:
            return 
        
        task_manager.edit_task(self.id, "completed", "True")
        self.update_task()

        default_category.remove_card(self)
        completed_category.add_card(self)
        print("Task Completed")

    def on_edit_click(self):
        """Opens a pop-up window to edit the task details."""
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Task")
        edit_window.geometry("300x200")
        edit_window.configure(bg="white")

        tk.Label(edit_window, text="Edit Task Name:", bg="white").pack(pady=5)
        name_entry = tk.Entry(edit_window)
        name_entry.insert(0, self.task.title)
        name_entry.pack(pady=5)

        tk.Label(edit_window, text="Edit Due Date:", bg="white").pack(pady=5)
        date_entry = tk.Entry(edit_window)
        date_entry.insert(0, self.task.due_date)
        date_entry.pack(pady=5)

        def save_changes():
            new_title = name_entry.get()
            new_due_date = date_entry.get()
            if new_title and new_due_date:
                # Update task in the backend
                task_manager.edit_task(self.id, "title", self.task.title)
                task_manager.edit_task(self.id, "due_date", self.task.due_date)

                # Refresh task in the frontend
                self.update_task()

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
        task_manager.delete_task(self.id)
        self.task = None
        self.destroy()
        print("Task Deleted")
    

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
        height = ((self.CARD_SIZE[1] + self.INTERIOR_PADDING[1] + 40) * self.CARD_DISPLAY_SIZE) 

        self.configure(bg="grey", height=height, width=width, bd=3, relief=tk.RAISED) 
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
        row_num = len(self.cards)
        self.cards.append(card)
        if row_num >= 3: 
            return
        card.grid(column=0, row=row_num, pady=5, padx=10, in_=self.card_frame)
        self.update_idletasks()

    def remove_card(self, card: TaskCard):
        if card not in self.cards:
            return
        card.grid_forget()  
        self.cards.remove(card)  
        self.rearrange_cards()

    def rearrange_cards(self):
        for index, card in enumerate(self.cards):
            if index < 2:
                card.grid(row=index)  
            elif index == 2:
                card.grid(column=0, row=index, pady=5, padx=10, in_=self.card_frame)
            else:
                card.grid_forget()

    

class AddTaskButton(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        complete = tk.Button(self, width=10, text="Add Task", font=("Arial", 12), bg="cornflowerblue", command=self.on_click)
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
            default_category.add_card(TaskCard(root, Task(title.get(), description.get(), priority.get(), due_date.get(), category.get())))
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

# Add Task Button
add_button = AddTaskButton(root)
add_button.grid(row=0, column=0, padx=20)

default_category = CategoryContainer(root, "Default")
default_category.grid(row=0, column=1, padx=30, pady=30)

completed_category = CategoryContainer(root, "Completed")
completed_category.grid(row=0, column=2, padx=30, pady=30)

# Example Task Card
default_category.add_card(TaskCard(root, Task("2450 HW", "Do Milestone 3", 0, "March 10", "School")))
default_category.add_card(TaskCard(root, Task("2700 HW", "Do Simulations", 2, "March 11", "School")))
default_category.add_card(TaskCard(root, Task("2010 HW", "Do Paper", 5, "March 12", "School")))

root.mainloop()

# Create and display Task_Card inside root
# card = TaskCard(root)
# card.grid(padx=20, pady=20)  

# card2 = TaskCard(root)
# card2.grid(padx=30, pady=30) 

# school = CategoryContainer(root, "School")
# school.grid(row=0, column=0, padx=30, pady=30)

# school.add_card(TaskCard(root, task1))
# # school.add_card(TaskCard(root))
# # school.add_card(TaskCard(root))

# work = CategoryContainer(root, "Work")
# work.grid(row=0, column=1, padx=30, pady=30)
# work.add_card(TaskCard(root))
# # work.add_card(TaskCard(root))
# # work.add_card(TaskCard(root))

 

