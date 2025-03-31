import tkinter as tk
from tkinter import messagebox
from task import Task
from task_master import TaskMaster
import tkinter.simpledialog as simpledialog

task_manager = TaskMaster()

class TaskCard(tk.Frame):
    def __init__(self, root, task: Task):
        super().__init__(root)  # Initialize the parent Frame
        self.root = root
        self.id = task.id
        self.task = task
        task_manager.add_task(task)

        self.configure(bg="lightblue",height=150, width=240, padx=10, pady=10,bd=3, relief=tk.RAISED)  # Set background and padding
        self.initialize_elements()

    
    def initialize_elements(self):
        self.task_name = tk.Label(self, text=self.task.title, font=( "Arial", 24), bg="lightblue")  
        self.task_name.grid(column=0,row=0,columnspan=2)

        self.due_date = tk.Label(self, text=self.task.due_date, font=( "Arial", 14), background="lightblue")
        self.due_date.grid(column=0, row=1, columnspan=2)

        self.canvas = tk.Canvas(self, width=180, height=5, highlightthickness=0, bg="lightblue")
        self.canvas.grid(column=0, row=2, columnspan=2, pady=(5, 5))

        self.canvas.create_line(10, 2, 230, 2, fill="black", width=2)

        self.show_more = tk.Button(self, width=10, text="Show More", font=("Arial", 12), bg="lightgreen", command=self.on_show_more_click)
        self.show_more.grid(column=0, row=3, columnspan=2)


    def on_show_more_click(self):
        self.show_more.destroy()

        self.complete = tk.Button(self, width=10, text="Complete", font=("Arial", 12), bg="green", command=self.on_complete_click)
        self.complete.grid(column=0, row=3, columnspan=2)

        self.edit = tk.Button(self, width=5, text="Edit", font=("Arial", 12), bg="azure4", fg="black", command=self.on_edit_click)
        self.edit.grid(column=0, row=4, pady=5)

        self.delete = tk.Button(self, width=5, text="Delete", font=("Arial", 12), bg="azure4", command=self.on_delete_click)
        self.delete.grid(column=1, row=4)

        self.add_tag = tk.Button(self, text="Add Tag", font=("Arial", 10), bg="lightgreen", command=self.on_add_tag_click)
        self.add_tag.grid(column=0, row=5, columnspan=1)

        self.show_less = tk.Button(self, text="Show Less", font=("Arial", 10), bg="lightgreen", command=self.on_show_less_click)
        self.show_less.grid(column=1, row=5, columnspan=1)

        self.attached_tags_label = tk.Label(self, text="Tags: None", font=("Arial", 10), bg="lightblue", anchor='w', wraplength=150)
        self.attached_tags_label.grid(column=0, row=6, columnspan=2, sticky='w')
        self.update_tags_label()


    def on_show_less_click(self):
        self.complete.destroy()
        self.edit.destroy()
        self.delete.destroy()
        self.add_tag.destroy()
        self.show_less.destroy()
        self.attached_tags_label.destroy()
        self.initialize_elements()
        

    def update_task(self):
        self.task = task_manager.get_task(self.id)


    def on_complete_click(self):
        self.on_show_less_click()
        if self.task.completed:
            return
        
        task_manager.edit_task(self.task.id, "completed", "True")
        default_category.remove_card(self)
        completed_category.add_card(self)
                    

    def on_edit_click(self):
        """Opens a pop-up window to edit the task details."""
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Task")
        edit_window.geometry("300x250")
        edit_window.configure(bg="darkorange")

        tk.Label(edit_window, text="Edit Task Name:").pack(pady=5)
        name_entry = tk.Entry(edit_window)
        name_entry.insert(0, self.task.title)
        name_entry.pack(pady=5)

        tk.Label(edit_window, text="Edit Due Date:").pack(pady=5)
        date_entry = tk.Entry(edit_window)
        date_entry.insert(0, self.task.due_date)
        date_entry.pack(pady=5)

        def save_changes(event=None):
            new_title = name_entry.get()
            new_due_date = date_entry.get()
            if new_title and new_due_date:
                # Update task in the backend

                task_manager.edit_task(self.task.id, "title", new_title)
                task_manager.edit_task(self.task.id, "due_date", new_due_date)

                # Refresh task in the frontend
                self.update_idletasks()

                # Update UI labels
                self.task_name.config(text=new_title)
                self.due_date.config(text=new_due_date)

                edit_window.destroy()
                print("Task updated!")

        edit_window.bind("<Return>", save_changes)

        save_button = tk.Button(edit_window, text="Save", command=save_changes)
        save_button.pack(pady=10)

        cancel_button = tk.Button(edit_window, text="Cancel", command=edit_window.destroy)
        cancel_button.pack(pady=5)

        print("Editing task...")

    def on_delete_click(self):
        task_manager.delete_task(self.task.id)
        if self.task.completed:
            completed_category.remove_card(self)
        else:
            default_category.remove_card(self)

        self.task = None
        print("Task Deleted")
    
    def on_add_tag_click(self):
        tag_window = tk.Toplevel(self.root)
        tag_window.title("Add Tag")
        tag_window.geometry("300x150")
        
        tk.Label(tag_window, text="Tag Title:").pack(pady=5)
        title_entry = tk.Entry(tag_window)
        title_entry.pack(pady=5)
        
        def add_tag(event=None):
            title = title_entry.get().strip()
            if title:
                self.task.add_tag(title)
                # Update backend
                task_manager.update_task_with_tag(self.task.id, title)
                self.update_tags_label()
                tag_window.destroy()
        
        tag_window.bind("<Return>", add_tag)
        tk.Button(tag_window, text="Add Tag", command=add_tag).pack(pady=10)
    
    def update_tags_label(self):
        if self.task.tags:
            self.attached_tags_label.config(text="Tags: " + ", ".join(self.task.tags))
        else:
            self.attached_tags_label.config(text="Tags: None")

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
        self.update_idletasks()

    def rearrange_cards(self):
        for index, card in enumerate(self.cards):
            if index < 3:
                card.grid(column=0, row=index, pady=5, padx=10, in_=self.card_frame)
            else:
                card.grid_forget()
        self.update_idletasks()


class AddTaskButton(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        complete = tk.Button(self, width=10, text="Add Task", font=("Arial", 12), bg="cornflowerblue", command= self.on_click)
        complete.grid(column=0, row=0)

    def on_click(self):
        input_window = tk.Toplevel(self)
        input_window.wm_title("Add New Task")

        title = tk.StringVar()
        description = tk.StringVar()
        priority = tk.StringVar()
        due_date = tk.StringVar()
        tags = tk.StringVar()

        title_label = tk.Label(input_window, text = 'Title')
        title_entry = tk.Entry(input_window, textvariable=title)

        description_label = tk.Label(input_window, text='Description')
        description_entry = tk.Entry(input_window, textvariable=description)

        priority_label = tk.Label(input_window, text='Priority')
        priority_entry = tk.Entry(input_window, textvariable=priority)

        due_date_label = tk.Label(input_window, text='Due Date')
        due_date_entry = tk.Entry(input_window, textvariable=due_date)

        tags_label = tk.Label(input_window, text='Tags')
        tags_entry = tk.Entry(input_window, textvariable=tags)

        def submit(event=None):
            default_category.add_card(TaskCard(root, Task(title.get(), description.get(), priority.get(), due_date.get(),
                                                           tags=[tag.strip() for tag in tags.get().split(',')])))
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

        tags_label.grid(row=4, column=0)
        tags_entry.grid(row=4, column=1)

        submit_button.grid(row=5, column=0, columnspan=2)

        input_window.bind("<Return>", submit)

        
class LoadButton(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        load_button = tk.Button(self, width=10, text="Load", font=("Arial", 12), bg="cornflowerblue", command=self.load)
        load_button.grid(column=0, row=0)

    def load(self):
        task_manager.load()
        for task in task_manager.get_tasks().values():
            if task.completed:
                completed_category.add_card(TaskCard(self.root, task))
            else:
                default_category.add_card(TaskCard(self.root, task))
        print("Tasks Loaded Successfully!")

    class SaveButton(tk.Frame):
        def __init__(self, root):
            super().__init__(root)
            self.root = root
            load_button = tk.Button(self, width=10, text="Save", font=("Arial", 12), bg="cornflowerblue", command=self.save)
            load_button.grid(column=0, row=0)

        def save(self):
            task_manager.save()
            print("Save!")

def on_close(root):
    # Create a confirmation window (popup)
    result = tk.messagebox.askyesno("Save Changes", "Do you want to save your changes?")
    
    # If the user clicks "Yes", run the save function
    if result:
        task_manager.save()
        root.quit()  # Close the main window
    else:
        root.quit()  # Close the window without saving


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

task_manager.load()
for task in task_manager.get_tasks().values():
    if task.completed:
        completed_category.add_card(TaskCard(root, task))
    else:
        default_category.add_card(TaskCard(root, task))

root.protocol("WM_DELETE_WINDOW", lambda: on_close(root))

root.mainloop()
