import tkinter as tk
from task import Task
from task_master import TaskMaster

class TaskCard(tk.Frame):
    def __init__(self, root):
        super().__init__(root)  # Initialize the parent Frame
        self.root = root

        # Create a frame inside Task_Card
        self.configure(bg="lightblue",height=150, width=200, padx=20, pady=20,bd=3, relief=tk.RAISED)  # Set background and padding
        self.grid_propagate(False)
        
        # Create a label inside the frame for visibility
        task_name = tk.Label(self, text="Task Card", font=( "Arial", 24), bg="lightblue")
        task_name.grid(column=0,row=0)

        due_date = tk.Label(self, text="xx/xx/xxxx", font=( "Arial", 14), background="lightblue")
        due_date.grid(column=0, row=1)

        canvas = tk.Canvas(self, width=200, height=4, highlightthickness=0)
        canvas.grid(column=0, row=3)

        canvas.create_line(0, 50, 200, 50, fill="black")
        

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
root.title("GUI")

task_manager = TaskMaster()

# Create and display Task_Card inside root
# card = TaskCard(root)
# card.grid(padx=20, pady=20)  # Ensures it appears in the window

# card2 = TaskCard(root)
# card2.grid(padx=30, pady=30) 

school = CategoryContainer(root, "School")
school.grid(row=0, column=0, padx=30, pady=30)
school.add_card(TaskCard(root))
school.add_card(TaskCard(root))
school.add_card(TaskCard(root))

work = CategoryContainer(root, "Work")
work.grid(row=0, column=1, padx=30, pady=30)
work.add_card(TaskCard(root))
work.add_card(TaskCard(root))
work.add_card(TaskCard(root))

addTask = AddTaskButton(root)
addTask.grid(padx=30, pady=30) 

root.mainloop()