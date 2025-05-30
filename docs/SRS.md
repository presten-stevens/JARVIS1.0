# Software Requirements Specification

## User Stories
1.  As a user, I should be able to add tasks so that I can have my own tasks in the system.
2.  As a user, I should be able to remove tasks so that I can get rid of tasks that are no longer relevant to me. 
3.  As a user, I should be able to edit tasks so I can correct mistakes or add new information without having to recreate the task.
4.  As a user, I should be able to move tasks so that I can keep my list more organized
5.  As a user, I should be able to complete tasks so that I can keep track of progress
6.  As a user, I should be able to set priority to my tasks so that I can keep track of whats most important
7.  As a user, I should be able to see notifications on tasks coming up on their due date so I can keep up on my day to day duties
8.  As a user, I should be able to see my overall progess of my tasks completed for the day/week
9.  As a user, I should be able to look at previously completed tasks so I can see how effective I've been
10. As a user, I should be able to connect to Google Calendar so that I can have all of my tasks in one spot.
11. As a user, I should be able to recieve positive reinforcement upon task completion so that I am empowered to achieve my tasks and goals.
12. As a user, I should be able to have AI prioritize my tasks so that I can know which tasks are most important without my input.
 

## Non-Functional Requirements
1. Data will be stored neatly and securely in a local JSON file
2. Notifications will be pushed even though the app isn't running

## Future Enhancements / Advanced Features
1. Google Calendar Integration
2. ChatGPT Integration
3. Positive Feedback Mechanisms (Streaks/Combos)

## Milestone 2 Update
Functional Requirement: 
- The CLI will allow the user to add, delete, view, save, and load tasks from a JSON file.

Nonfunctional Requirement: 
- The CLI (Command Line Interface) will load and save tasks without any sort of lag.

User Stories:
- As a user I can add tasks to create a list of todo items.
- As a user I can delete tasks I no longer need to keep track of.
- As a user I can view all of my tasks to keep organized and focused on what I need to do.
- As a user I can load my old tasks to help me keep track of long term tasks.

## UML Diagrams
### Class Diagram
![UMLv2](images/ClassDiagram.png)
[Lucid Chart Link](https://lucid.app/lucidchart/c17142f3-8754-414f-972a-95288ab84823/edit?viewport_loc=-117%2C-209%2C2105%2C1712%2C0_0&invitationId=inv_69c60722-b6b5-49e5-aef3-434c32440ed2)

### Use Case Diagram
![usecaseV1](images/usecaseV1.png)

### Sequence Diagram 
![SequenceV2](images/sequenceV2.png)

### Proof of ZenHub
![ZenHub](../.zenhub_status/zenhubScreenshotMilestone3.png)

## Milestone 4 Update
Functional Requirment:
- Users can add tags to tasks to help organize them
- Users can organize the tasks by the tags

Nonfunctional Requirment:
- Dates must be stored in a specific format to allow for future integration

User Stories:
- As a user I can add tags to my tasks
- As a user I can sort my tasks by the different tags
- As a user I can see all the information (Description, Due date, etc,.) of my task 

### Sequence Diagram 
![SequenceV3](images/sequenceV3.png)
