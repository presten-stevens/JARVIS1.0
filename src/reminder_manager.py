from datetime import datetime, timedelta
import time
import tkinter as tk

reminder_date = datetime(year=2025, month=4, day=14, hour=15, minute=59)


class ReminderManager():
    def __init__(self):
        self.reminders = []

    def add_reminder(self, message: str, time: datetime):
        self.reminders += Reminder(message, time)


class Reminder():
    def __init__(self, message: str, time: datetime):
        self.message = message
        self.time = time

date_has_passed = False
while (not date_has_passed): 
    print("Checking time!")
    date_has_passed = ((reminder_date - datetime.now()) / timedelta(seconds=1)) < 0
    time.sleep(5)

print("Date has passed!")