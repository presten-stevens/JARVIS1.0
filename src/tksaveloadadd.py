import tkinter as tk
from task_master import TaskMaster

def display_tasks(task_mngr: TaskMaster, label_frame: tk.Frame):
    """
    Displays the tasks in the task manager by clearing the old labels
    and adding new ones to the label frame.
    """
    # Clear any existing labels in the frame
    for widget in label_frame.winfo_children():
        widget.destroy()

    for task in task_mngr.tasks.values():
        label_str = f"Title: {task.title}\nDescription: {task.description}\nDue Date: {task.dueDate}"
        label = tk.Label(label_frame, text=label_str)
        label.pack(pady=5)



def main():
    root = tk.Tk()
    root.title("Task Master")
    frame = tk.Frame(root)

    task_master = TaskMaster()

    # Create the main window
    root.title("Task Master Desktop Application")
    root.geometry("3000x2000")


    
    
    viewBtn = tk.Button(root, text="View Tasks", command=lambda: display_tasks(task_master, frame))
    viewBtn.pack(pady=5)
    frame.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()