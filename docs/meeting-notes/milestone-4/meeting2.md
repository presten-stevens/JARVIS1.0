# Monday March 31st


## Attendance

- [X] Joshua LeVar
- [X] Presten Stevens
- [] Ben Oakeson
- [X] Adam Sellers

## Recap
  Feature from peer review added. Received feedback that save and load should happen automatically. Change was made prior to this meeting.
  Other notable changes prior to meeting:
    Task_Master.add_task() takes a Task object instead of all of the necessary variables to make one.
    ID's have been changed to be an attribute of Task, so that the TaskMaster.tasks dictionary can populate with consistency
    Tags can now be added to tasks. Plan to add task filtering based on tag in place.
    ID changes fixed some bugs that were showing in the GUI.
    save_test.py removed

## Decisions
  Determined that priority sort was the most important deliverable item for sorting. 
  Design includes a SORTMODE for TaskMaster so that other sorting methods can be implemented.
  Plan to add constraints to user input to prepare for final sprint adding sort by date.
  Optimizing test cases.

  3 Deliverable Advanced Features:
    Load on start/save on quit
    Add tags to tasks / filter based on tag
    Sort by priority upon loading


## Future Decisions
    Task_Cards OOP cleanup change to main function


## Final Notes
    Code is much more scalable and ready to face milestone 5.

