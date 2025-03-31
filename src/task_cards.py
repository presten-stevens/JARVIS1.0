import tkinter as tk
from tkinter import messagebox
from task import Task
from task_master import TaskMaster
from abc import ABC, abstractmethod
from datetime import datetime

task_manager = TaskMaster()

class Editer(ABC):
    """Helps edit cards or add new cards"""
    @abstractmethod
    def information(self):
        pass

class EditCard(Editer):
    def __init__(self, task, task_card):
        self.task = task
        self.task_card = task_card

    def information(self, root, name_entry, description_entry, priority_entry, date_entry, category_entry):
        new_title = name_entry
        new_due_date = date_entry
        new_priority = priority_entry
        new_category = category_entry
        new_description = description_entry

        if new_title and new_due_date:
            task_manager.edit_task(self.task.id, "title", new_title)
            task_manager.edit_task(self.task.id, "due_date", new_due_date)
            task_manager.edit_task(self.task.id, "priority", new_priority)
            task_manager.edit_task(self.task.id, "category", new_category)
            task_manager.edit_task(self.task.id, "description", new_description)

            # Refresh UI after edit
            self.task_card.refresh()

class NewCard(Editer):
    def information(self, root, title, description, priority, due_date, category):
        default_category.add_card(TaskCard(root, Task(title, description, priority, due_date, category))) 


class TaskCard(tk.Frame):
    def __init__(self, root, task: Task):
        super().__init__(root)  
        self.root = root
        self.task = task
        task_manager.add_task(task)

        self.configure(bg="lightblue",height=150, width=240, padx=10, pady=10,bd=3, relief=tk.RAISED)  # Set background and padding
        
        self.task_name = tk.Label(self, text=self.task.title, font=( "Arial", 24), bg="lightblue")  
        self.task_name.grid(column=0,row=0,columnspan=2)

        self.due_date = tk.Label(self, text=self.task.due_date, font=( "Arial", 14), background="lightblue")
        self.due_date.grid(column=0, row=1, columnspan=2)

        self.canvas = tk.Canvas(self, width=180, height=5, highlightthickness=0, bg="lightblue")
        self.canvas.grid(column=0, row=2, columnspan=2, pady=(5, 5))

        self.canvas.create_line(10, 2, 230, 2, fill="black", width=2)

        self.complete = tk.Button(self, width=10, text="Complete", font=("Arial", 12), bg="green", command=self.on_complete_click)
        self.complete.grid(column=0, row=3, columnspan=2)
        
        self.edit_button = AddTaskButton(self, "edit task", new_card=EditCard(self.task, self), col=0, row=4, width=5)
        self.delete = tk.Button(self, width=5, text="Delete", font=("Arial", 12), bg="azure4", command=self.on_delete_click)
        self.edit_button.grid(column=0, row=4)
        self.delete.grid(column=1, row=4)

    def refresh(self):
        """Updates the UI to reflect the task's new data."""
        self.task_name.config(text=self.task.title)
        self.due_date.config(text=self.task.due_date)

    def on_complete_click(self):
        if self.task.completed:
            return 
        
        task_manager.edit_task(self.task.id, "completed", "True")
        default_category.remove_card(self)
        completed_category.add_card(self)
        print("Task Completed")

    # def save_changes(self):
        
    #     self.task_name.config(text=self.title)
    #     self.due_date.config(text=new_due_date)


    def on_edit_click(self):
        """Opens a pop-up window to edit the task details."""
        edit_button = AddTaskButton(root, "edit task")
        edit_button.grid(pady=10)
        # edit_window = tk.Toplevel(self.root)
        # edit_window.title("Edit Task")
        # edit_window.geometry("300x200")
        # edit_window.configure(bg="white")

        # tk.Label(edit_window, text="Edit Task Name:", bg="white").pack(pady=5)
        # name_entry = tk.Entry(edit_window)
        # name_entry.insert(0, self.task.title)
        # name_entry.pack(pady=5)

        # tk.Label(edit_window, text="Edit Due Date:", bg="white").pack(pady=5)
        # date_entry = tk.Entry(edit_window)
        # date_entry.insert(0, self.task.due_date)
        # date_entry.pack(pady=5)

        # 
        # save_button = tk.Button(edit_, text="Save", bg="green", fg="white", command=save_changes)
        # save_button.pack(pady=10)

        # cancel_button = tk.Button(edit_window, text="Cancel", bg="red", fg="white", command=edit_window.destroy)
        # cancel_button.pack(pady=5)

        # print("Editing task...")

    def on_delete_click(self):
        task_manager.delete_task(self.task.id)
        if self.task.completed:
            completed_category.remove_card(self)
        else:
            default_category.remove_card(self)

        self.task = None
        print("Task Deleted")


class CategoryContainer(tk.Frame):
    INTERIOR_PADDING = (20, 20)
    CARD_SIZE = (200, 150)
    CARD_DISPLAY_SIZE = 3
    
    def __init__(self, root, category_name: str):
        super().__init__(root)  
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


class InputChecker(ABC):
    @abstractmethod
    def checkObject(self):
        pass

class CheckTitle(InputChecker):
    def checkObject(self, title):
        if title == "":
            return False 
        else:
            return True 
        
class CheckDescription(InputChecker):
    def checkObject(self, description):
        if description == "":
            return False
        else:
            return True 

class CheckPriority(InputChecker):
    def checkObject(self, priority):
        if( not priority.isdigit() or not int(priority) > 0):
            return False
        else:
            return True 
        
class CheckDate(InputChecker):
    def checkObject(self, date):
        format = "%d-%m-%Y"
        try: 
            result = bool(datetime.strptime(date, format))
        except ValueError:
            result = False
        return result

class CheckCategory(InputChecker):
    def checkObject(self, Category):
        if(Category == ""):
            return False
        else:
            return True

class AddTaskButton(tk.Frame):
    def __init__(self, root, title:str, new_card:Editer, col=0, row=0, width=10) :
        super().__init__(root)
        self.new_card = new_card
        self.root = root
        self.title = title
        complete = tk.Button(self, width=width, text=title, font=("Arial", 12), bg="cornflowerblue", command= self.on_click)
        complete.grid(column=col, row=row)

    def on_click(self):
        input_window = tk.Toplevel(self)
        input_window.wm_title(self.title)

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
            title_checker = CheckTitle()
            description_checker = CheckDescription()
            priority_checker = CheckPriority()
            date_checker = CheckDate()
            category_checker = CheckCategory()

            valid = True

            if not title_checker.checkObject(title.get()):
                title_entry.config(bg="red")
                valid = False
            else:
                title_entry.config(bg="white")

            if not description_checker.checkObject(description.get()):
                description_entry.config(bg="red")
                valid = False
            else:
                description_entry.config(bg="white")

            if not priority_checker.checkObject(priority.get()):
                priority_entry.config(bg="red")
                valid = False
            else:
                priority_entry.config(bg="white")

            if not date_checker.checkObject(due_date.get()):
                due_date_entry.config(bg="red")
                valid = False
            else:
                due_date_entry.config(bg="white")

            if not category_checker.checkObject(category.get()):
                category_entry.config(bg="red")
                valid = False
            else:
                category_entry.config(bg="white")
            if valid:
                self.new_card.information(root, title.get(), description.get(), priority.get(), due_date.get(), category.get())
                input_window.destroy()
                self.update_idletasks()
                

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


        
class LoadButton(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        load_button = tk.Button(self, width=10, text="Load", font=("Arial", 12), bg="cornflowerblue", command=self.load)
        load_button.grid(column=0, row=0)

    def load(self):
        task_manager.load()
        for task in task_manager.get_tasks().values():
            print(id, task)
            if task.completed:
                completed_category.add_card(TaskCard(self.root, task))
            else:
                print("NOT COMPLETE")
                default_category.add_card(TaskCard(self.root, task))
        print("LOAD!")

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
add_button = AddTaskButton(root, "Add New Task", new_card = NewCard())
add_button.grid(row=0, column=0, padx=20)

default_category = CategoryContainer(root, "Default")
default_category.grid(row=0, column=1, padx=30, pady=30)

completed_category = CategoryContainer(root, "Completed")
completed_category.grid(row=0, column=2, padx=30, pady=30)

task_manager.load()
for task in task_manager.get_tasks().values():
    print(id, task)
    if task.completed:
        completed_category.add_card(TaskCard(root, task))
    else:
        print("NOT COMPLETE")
        default_category.add_card(TaskCard(root, task))

root.protocol("WM_DELETE_WINDOW", lambda: on_close(root))

root.mainloop()
    






