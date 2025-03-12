import tkinter as tk

class Task_Card(tk.Frame):
    def __init__(self, root):
        super().__init__(root)  # Initialize the parent Frame
        self.root = root

        # Create a frame inside Task_Card
        self.configure(bg="lightblue",height=150, width=240, padx=10, pady=10,bd=3, relief=tk.RAISED)  # Set background and padding
        # self.grid_propagate(False)
        
        # Create a label inside the frame for visibility
        task_name = tk.Label(self, text="Task Card", font=( "Arial", 24), bg="lightblue")
        task_name.grid(column=0,row=0,columnspan=2)

        due_date = tk.Label(self, text="xx/xx/xxxx", font=( "Arial", 14), background="lightblue")
        due_date.grid(column=0, row=1, columnspan=2)

        canvas = tk.Canvas(self, width=180, height=5, highlightthickness=0, bg="lightblue")
        canvas.grid(column=0, row=2, columnspan=2, pady=(5, 5))

        canvas.create_line(10, 2, 230, 2, fill="black", width=2)

        complete = tk.Button(self, width=10, text="Complete", font=("Arial", 12), bg="green", command=self.on_complete_click)
        complete.grid(column=0, row=3, columnspan=2)
        
        edit = tk.Button(self, width=5, text="Edit", font=("Arial", 12), bg="blue", fg="black", command=self.on_edit_click)
        delete = tk.Button(self, width=5, text="Delete", font=("Arial", 12), bg="blue", command=self.on_delete_click)
        edit.grid(column=0, row=4)
        delete.grid(column=1, row=4)

    def on_complete_click(self):
        print("complete!!")

    def on_edit_click(self):
        print("edit!!")

    def on_delete_click(self):
        print("delete!!")
    

# Create main application window
root = tk.Tk()
root.title("GUI")

# Create and display Task_Card inside root
card = Task_Card(root)
card.grid(padx=20, pady=20)  # Ensures it appears in the window

root.mainloop()