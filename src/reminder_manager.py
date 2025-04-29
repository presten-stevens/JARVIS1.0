from datetime import datetime, timedelta
import tkinter as tk


class Reminder():
    def __init__(self, message: str, time: datetime):
        self.message = message
        self.time = time

    def __str__(self):
        return f"Reminder for ({self.time}):\n{self.message}"


class ReminderManager():
    def __init__(self, root: tk.Tk):
        self.root = root
        self.observer = None
        self.reminders = []

    def add_observer(self, observer):
        self.observer = observer

    def add_reminder(self, message: str, time: datetime):
        self.reminders.append(Reminder(message, time))
        if len(self.reminders) == 1:
            self.run_clock()

    def run_clock(self):
        print(f"[{len(self.reminders)}] Checking at {datetime.now()}")
        for reminder in self.reminders:
            if ((reminder.time - datetime.now()) / timedelta(seconds=1)) < 0:
                self.observer.send_notification(reminder)
                self.reminders.remove(reminder) 

        if self.reminders:
            self.root.after(10000, lambda : self.run_clock())


class Notifier():
    def __init__(self, manager: ReminderManager):
        self.manager = manager
        self.manager.add_observer(self)

    def send_notification(self, reminder):
        print(f"Sending Notification for:\n{reminder}")
        
        popup_window = tk.Toplevel(self.manager.root)
        popup_window.title("Notification")

        tk.Label(popup_window, text=reminder).pack(pady=5)
        tk.Button(popup_window, text="Okay", command=popup_window.destroy).pack(pady=5)

