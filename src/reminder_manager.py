from datetime import datetime, timedelta
import time
import tkinter as tk


##TODOS

# Connect to tkinter
# Turn off clock when there are no reminders

class Reminder():
    def __init__(self, message: str, time: datetime):
        self.message = message
        self.time = time

    def __str__(self):
        return f"Reminder for ({self.time}): {self.message}"


class ReminderManager():
    def __init__(self):
        self.observer = None
        self.reminders = []

    def add_observer(self, observer):
        self.observer = observer

    def add_reminder(self, message: str, time: datetime):
        self.reminders.append(Reminder(message, time))

    def run_clock(self):
        while (True): 
            print(f"[{len(self.reminders)}] Checking at {datetime.now()}")
            for reminder in self.reminders:
                if ((reminder.time - datetime.now()) / timedelta(seconds=1)) < 0:
                    self.observer.send_notification(reminder)
                    self.reminders.remove(reminder) 
            time.sleep(10)


class Notifier():
    def __init__(self, manager: ReminderManager):
        self.manager = manager
        self.manager.add_observer(self)

    def send_notification(self, reminder):
        print(f"Sending Notification for: {reminder}")

reminder_manager = ReminderManager()
mynotifier = Notifier(reminder_manager)

reminder_manager.add_reminder("Yippee!", datetime(year=2025, month=4, day=14, hour=16, minute=23))
reminder_manager.add_reminder("Hooray!", datetime(year=2025, month=4, day=14, hour=16, minute=24))
reminder_manager.add_reminder("Wahoo!", datetime(year=2025, month=4, day=14, hour=16, minute=25))

reminder_manager.run_clock()
