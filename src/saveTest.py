import task_master
import sys

def save():
    master = task_master.task_master()
    master.tasks.append(task_master.task("task1", "task1desc"))
    master.tasks.append(task_master.task("task2", "task2desc"))
    master.tasks.append(task_master.task("task3", "task3desc"))
    master.tasks.append(task_master.task("task4", "task4desc"))
    master.tasks.append(task_master.task("task5", "task5desc"))
    master.save()



def load():
    master = task_master.task_master()
    master.load()
    master.printf()

def main(arg):
    if arg == "save":
        save()
    elif arg == "load":
        load()
    else:
        print("Usage: python3 saveTest.py save/load")

if __name__ == "__main__":
    main(sys.argv[1])