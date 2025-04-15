import tkinter as tk
import calendar
from datetime import datetime
from src.task_master import TaskMaster



class Day(tk.Frame):
    def __init__(self, master, day_number, tasks=None):
        super().__init__(master, borderwidth=1, relief="solid", width=100, height=100)
        self.day_number = day_number
        self.tasks = tasks or []

        self.grid_propagate(False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.day_label = tk.Label(self, text=str(day_number), font=("Arial", 9, "bold"))
        self.day_label.place(relx=0, rely=0, anchor="nw", x=4, y=2)

        self.populate_tasks()

    def populate_tasks(self):
        for i, task in enumerate(self.tasks[:3]):  
            label = tk.Label(self, text=task.title, font=("Arial", 7), bg="#d1ecf1", wraplength=90)
            label.place(x=4, y=20 + i*15, anchor="nw")


class CalendarView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        task_master = TaskMaster()
        task_master.load()
        self.title("Calendar")
        self.tasks = task_master.get_tasks()
        print(self.tasks)
        self.create_outline()

    def get_tasks_for_day(self, day, month, year):
        matched = []
        for task in self.tasks.values():
            try:
                d = datetime.strptime(task.due_date, "%d/%m/%Y")
                if d.day == day and d.month == month and d.year == year:
                    matched.append(task)
            except Exception as e:
                print(f"Skipping task with invalid date: {e}")
        return matched
    
    def create_outline(self):
        now = datetime.today()
        cal = calendar.monthcalendar(now.year, now.month)

        header = tk.Label(self, text=now.strftime("%B %Y"), font=("Arial", 14, "bold"))
        header.grid(row=0, column=0, columnspan=7, pady=(10, 5))

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            tk.Label(self, text=day, font=("Arial", 10, "bold")).grid(row=1, column=i, padx=2, pady=2)

        for r, week in enumerate(cal, start=2):
            for c, day in enumerate(week):
                if day == 0:
                    empty = tk.Frame(self, width=60, height=60)
                    empty.grid(row=r, column=c, padx=1, pady=1)
                    continue

                tasks_today = self.get_tasks_for_day(day, now.month, now.year)
                day_frame = Day(self, day, tasks_today)
                day_frame.grid(row=r, column=c, padx=1, pady=1)