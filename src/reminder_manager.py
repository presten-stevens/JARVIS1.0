from datetime import datetime, timedelta
import time
import tkinter as tk


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
            print(f"Checking time at {datetime.now()}")
            print(len(self.reminders))
            for reminder in self.reminders:
                print(reminder)
                if ((reminder.time - datetime.now()) / timedelta(seconds=1)) < 0:
                    print("BLEEB BLORP!!")
                    self.observer.send_notification(reminder)
                    self.reminders.remove(reminder) 
            time.sleep(10)


class Notifier():
    def __init__(self, manager: ReminderManager):
        self.manager = manager
        self.manager.add_observer(self)

    def send_notification(self, reminder):
        print(f"Sending Notification for: {reminder}")

karl = ReminderManager()
mynotifier = Notifier(karl)

karl.add_reminder("Yippee!", datetime(year=2025, month=4, day=14, hour=16, minute=22))
karl.add_reminder("Hooray!", datetime(year=2025, month=4, day=14, hour=16, minute=23))
karl.add_reminder("Wahoo!", datetime(year=2025, month=4, day=14, hour=16, minute=24))

karl.run_clock()
