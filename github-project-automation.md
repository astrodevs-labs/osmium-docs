# Automating the GitHub Project Workflow


## List of things to automate:

### Developers Workflow:
1. Assign a new Issue to a developer
2. Assign a new PR to a developer when work is done
3. Ask review from at least 1 other team member when a PR is ready
3.1. If there are changes requested, the assigned dev should make the changes
4. If approved, Product Owner should review and Test
4.1 If Product Owner asks for changes, the previous reviewer(s) should make the changes (This will force reviewers to make quality reviews)

### Views:
 - RoadMap / Milestones (only Meta Issues)
 - Current sprint (only task issues)
 - Team Review (only PR and not PO reviewer)
 - Product Owner Review (only PR with PO reviewer)

### Developer Tasks and Sub Tasks Issues:

- [ ] Create a new card in 'To Do' when a new Issue is created
- [ ] Move card to 'In Progress' when a Issue is assigned to someone
- [ ] Move card to 'In Review' when a linked PR to an Issue as been asked for review
- [ ] Move card to 'Done' when an Issue is closed

- [ ] Create a new card in 'To Do' when a new PR is created
- [ ] Create (a Draft PR / a new card / a new branch) in 'To Do' when an Issue (Not meta issues) as been assigned
- [ ] Move card to 'In Progress' when a PR is assigned to someone
- [ ] Move card to 'In Review' when a PR as been asked for review
- [ ] Move card to 'Changes Requested' when a PR as been asked for changes or when CI fails
- [ ] Move card to 'PO Review' and assign the 'Product Owner' when a PR as been approved by at least one team reviewer
- [ ] Move card to 'Done' when a PR is merged/closed

### Meta Issues / Epic:
- [ ] Create a new card in 'To Do' when a new Meta Issue is created
- [ ] Parse an created all child 'task' issues from a Meta Issue ?
- [ ] Move card to 'In Progress' when a Meta Issue when a linked Issue is assigned to someone
- [ ] Move card to 'PO Review' when all issues linked to a Meta Issue are closed
- [ ] Move card to 'Done' when a Meta Issue is closed


-------------------------------
# Automating the GitHub Project Workflow

## Developers Workflow:

## List of type of card :
### Epic (Milestone)
This kind of workload will be described by github milestones. It should group User and Technical stories.

### User stories (Issue):
This type of issue will traduce a complete feature on a functional point of view (like open a file in the IDE). Those issues will track multiple "task" issues

### Technical stories (Issue):
This type of issue will describe a technical work set to do in order to keep the codebase viable. Those issues will track multiple "task" issues

### Bug (Issue):
This type of issue describe a reported bug. Those issue will track multiple "task" issues for reproducing and fixing stages.

### Task (Issue):
This type of issue will describe a technical task to achieve in order to advance on a Task/User story/Technical story.
A task may track other task (you can think of them as "subtasks"). 

## List of things to automate:

### Epic Milestone Issues:


### User Story Issues:
For each user story we need a branch in 'feature/'
The name of the branch will be in lowercase

### Tasks Issues:
For each user story we need a branch in 'feature/{User story}/'
If Not Meta Issue refer to Sub Tasks Issues !

- [ ] Create a new card in 'To Do' when a new Issue is created
- [ ] Move card to 'In Progress' when a Issue is assigned to someone

- [ ] Move card to 'In Review' when all linked Issues are closed
- [ ] Move card to 'Done' when an Issue is closed


- [ ] Create a new card in 'To Do' when a new PR is created

- [ ] Create (a Draft PR / a new card / a new branch) in 'To Do' when an Issue is opened.

- [ ] Move card to 'In Progress' when a sub issue is assigned to someone

- [ ] Assign a PO reviewer when all sub PR are merged and move card 'In Review'

- [ ] Move card to 'Changes Requested' when a PR as been asked for change

- [ ] Move card to 'PO Review' and assign the 'Product Owner' when a PR as been approved by at least one team reviewer

- [ ] Move card to 'Done' when a PR is merged/closed


### Sub Tasks Issues only:
For each user story we need a branch in 'feature/{User story}/{Task}/'

- [ ] Create a new card in 'To Do' when a new Issue is created
- [ ] Move card to 'In Progress' when a Issue is assigned to someone
- [ ] Move card to 'In Review' when a linked PR to an Issue as been asked for review
- [ ] Move card to 'Done' when an Issue is closed

- [ ] Create a new card in 'To Do' when a new PR is created
- [ ] Create (a Draft PR / a new card / a new branch) in 'To Do' when an Issue as been assigned
- [ ] Move card to 'In Progress' when a PR is assigned to someone
- [ ] Move card to 'In Review' when a PR as been asked for review
- [ ] Move card to 'Changes Requested' when a PR as been asked for changes or when CI fails
- [ ] Move card to 'PO Review' and assign the 'Product Owner' when a PR as been approved by at least one team reviewer
- [ ] Move card to 'Done' when a PR is merged/closed





