# Tuesday March 18th


## Attendance

- [X] Joshua LeVar
- [] Presten Stevens
- [] Ben Oakeson
- [X] Adam Sellers

## Action Plan
    Fix Bugs
        Bug 1 - Edit bugs (can't edit more than once sometimes?)
        Bug 2 - Load, adds onto existing cards

    Visual Bugs
        Fix grid so buttons are in-line
        Fix edit so it doesn't resize past frame


    Implement advanced features to enhance the Task Manager.
        Order by priority - As we load items or display them, we pull them from a list sorted by priority
        Add a clock to check if due date has passed (Get to streaks maybe, if not do streaks next sprint)

    Identify and apply design patterns to improve flexibility.
        Change Save to save as id-name.json instead of name.json (BEN tentative)
        Make it pretty (Josh? Ask for assistance)
        Make task_master a static class and change to class attribute interactions (cls instead of self) (PRESTEN)
        Make id an attribute of task, when we load tasks from json files, we can use id to assign as a key for the task_master.tasks dict (ADAM)
    
    Conduct integration testing to validate module interactions.
        Make test cases for each individual module, ensure there is low coupling/dependencies

    Update project artifacts, including diagrams, documentation, and Agile boards.
        Update ClassDiagram, sequence diagram, UML diagram
    
    Refine and optimize your code for maintainability and scalability.
        Make task_master a static class and change to class attribute interactions (cls instead of self)
        Make id an attribute of task, when we load tasks from json files, we can use id to assign as a key for the task_master.tasks dict
        it's possible that fixing this will fix some of the bugs experienced from save/load

    Engage in peer reviews to gain constructive feedback on your application.
        Ask in class tomorrow for feedback on our application thus far

## Decisions
    Make IDs an attribute of task
    Make TaskMaster a static class

## Future Decisions
    GUI final design
    Special Features

## Final Notes
    Good meeting, discussed some potential flaws in program scaleability, identified some bugs to be fixed, as well as potential features. Get everything assigned so far done by Tuesday.

