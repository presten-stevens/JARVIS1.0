import tkinter as tk
from tkinter import ttk
from datetime import datetime
import calendar 

class CalendarEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.date = tk.StringVar()
        super().__init__(master, textvariable=self.date, **kwargs)
        self.date.set(datetime.today().strftime("%d/%m/%Y"))

        self.bind("<Button-1>", self.show_calendar)

        self.top =None

    def show_calendar(self, event=None):
        if self.top and self.top.winfo_exists():
            return

        self.top = tk.Toplevel(self)
        self.top.wm_overrideredirect(True) 
        x = self.winfo_rootx()
        y = self.winfo_rooty() + self.winfo_height()
        self.top.geometry(f"+{x}+{y}")

        self.draw_calendar()
    
    def draw_calendar(self):
        now = datetime.today()

        cal = calendar.monthcalendar(now.year, now.month)
        header = tk.Label(self.top, text=now.strftime("%B %Y"), font=("Arial", 10, "bold"))
        header.grid(row=0, column=0, columnspan=7)

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            tk.Label(self.top, text=day).grid(row=1, column=i)

        for r, week in enumerate(cal, start=2):
            for c, day in enumerate(week):
                if day == 0:
                    continue
                b = tk.Button(self.top, text=str(day), width=3,
                              command=lambda d=day: self.set_date(now.year, now.month, d))
                b.grid(row=r, column=c, padx=1, pady=1)
    
    def set_date(self, year, month, day):
        chosen_date = datetime(year, month, day).strftime("%d/%m/%Y")
        self.date.set(chosen_date)
        self.top.destroy()
