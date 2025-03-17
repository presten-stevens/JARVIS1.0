import tkinter as tk
from task_master import TaskMaster

def display_tasks(task_mngr: TaskMaster, root: tk.Tk, label_frame: tk.Frame):
    """
    Displays the tasks in the task manager by clearing the old labels
    and adding new ones to the label frame.
    """
    # Clear any existing labels in the frame
    for widget in label_frame.winfo_children():
        widget.destroy()

    # Create new labels for the tasks
    labels = create_labels(task_mngr, root)

    # Pack the labels into the label frame
    for label in labels:
        label.pack(pady=5)

def load(root: tk.Tk, task_master: TaskMaster):
    task_master.load()
    print(task_master.tasks)

def save(root: tk.Tk, task_master: TaskMaster):
    task_master.save()
    print("saved")

def main():
    root = tk.Tk()
    root.title("Task Master")
    frame= tk.Frame(root)
    frame.pack(pady=20)

    task_master = TaskMaster()

    # Create the main window
    root.title("Task Master Desktop Application")
    root.geometry("3000x2000")


    loadBtn = tk.Button(root, text="Load", command=lambda: load(root, task_master))
    loadBtn.pack(pady=5)
    saveBtn = tk.Button(root, text="Save", command=lambda: save(root, task_master))
    saveBtn.pack(pady=5)
    viewBtn = tk.Button(root, text="View Tasks", command=lambda: display_tasks(task_master, root, frame))
    viewBtn.pack(pady=5)

    root.mainloop()
    '''
    # Set the size of the window (width x height)
    # Add a label widget to the window
    label = tk.Label(root, text="Enter your name:")
    label.pack(pady=10)  # Add some padding to the label

    # Add an entry widget to the window
    entry = tk.Entry(root)
    entry.pack(pady=5)  # Add some padding to the entry widget

    # Add a button widget that will call the update_label function
    button = tk.Button(root, text="Submit", command=lambda: update_label(entry, label))
    button.pack(pady=10)  # Add some padding to the button

    # Run the Tkinter event loop to display the window
    root.mainloop()
    '''

if __name__ == "__main__":
    main()