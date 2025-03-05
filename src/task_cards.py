import tkinter as tk

class Task_Card(tk.Frame):
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
        

# Create main application window
root = tk.Tk()
root.title("GUI")

# Create and display Task_Card inside root
card = Task_Card(root)
card.grid(padx=20, pady=20)  # Ensures it appears in the window

root.mainloop()