import task_master
import sys

def save():
    master = task_master.TaskMaster()
    master.tasks[1] = (task_master.Task("task1", "task1desc", 3, "10/4/3", "school"))
    master.tasks[2] = (task_master.Task("task2", "task2desc", 3, "10/4/3", "school"))
    master.tasks[3] = (task_master.Task("task3", "task3desc", 3, "10/4/3", "school"))
    master.tasks[4] = (task_master.Task("task4", "task4desc", 3, "10/4/3", "school"))
    master.tasks[5] = (task_master.Task("task5", "task5desc", 3, "10/4/3", "school"))
    master.save()



def load():
    master = task_master.TaskMaster()
    master.load()
    master.printf()

def main(arg):
    if arg == "save":
        save()
    elif arg == "load":
        load()
    else:
        print("Usage: python3 save_test.py save/load")

if __name__ == "__main__":
    main(sys.argv[1])