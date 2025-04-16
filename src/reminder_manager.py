from datetime import datetime, timedelta
import tkinter as tk
import json
import os

class Reminder():
    def __init__(self, message: str, time: datetime):
        self.message = message
        self.time = time

    def __str__(self):
        return f"Reminder for ({self.time}):\n{self.message}"
    
    def to_dict(self):
        return {
            'message': self.message,
            'time': self.time.isoformat()
        }

    @classmethod
    def from_dict(cls, dict):
        time = datetime.fromisoformat(dict['time'])
        return cls(dict['message'], time)
    

class ReminderManager():
    save_file = os.fsencode("saves/reminders.json")

    def __init__(self, root: tk.Tk):
        self.root = root
        self.observer = None
        self.clock_running = False

        if os.path.exists(self.save_file):
            with open(self.save_file, 'r') as f:
                data = json.load(f)
                self.reminders = [Reminder.from_dict(reminder_dict) for reminder_dict in data]
        else:
            self.reminders = []


    def add_observer(self, observer):
        self.observer = observer
        if not self.clock_running and self.reminders:
            self.run_clock()

    def add_reminder(self, message: str, time: datetime):
        self.reminders.append(Reminder(message, time))
        if not self.clock_running:
            self.run_clock()

    def run_clock(self):
        print(f"[{len(self.reminders)}] Checking at {datetime.now()}")
        self.clock_running = True
        for reminder in self.reminders:
            if ((reminder.time - datetime.now()) / timedelta(seconds=1)) < 0:
                self.observer.send_notification(reminder)
                self.reminders.remove(reminder) 

        if self.reminders:
            self.root.after(30000, lambda : self.run_clock())
        else:
            self.clock_running = False

    def save(self):
        with open(self.save_file, 'w') as f:
            json.dump([reminder.to_dict() for reminder in self.reminders], f)


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

