# Interaction summary

- on issue created (any installed repo) : add issue to management project
- on pr created (draft) : add pr to management and dev project in Todo and Waiting
- on card moved, management (to plan -> planned) : add to dev project and move card to hidden
- on pr opened (draft -> open) : user must ask review
- on pr review requested (non PO) : (management: move PR from todo to in review), (dev: move PR from wating to in review AND ISSUE to In PR)
- on pr changes requested : (management: move PR from any to changes requested), (dev: move PR from any to changes requested, move issue in To Verify)
- on pr changes approved (from non PO) : (management: move PR from in review to functionnal review), (dev: move PR and from in review to functionnal review) and automatically ask review of PO ?
- on pr changes approved (from PO) : (management: move PR to staging), (dev: move PR to staging and issue to Done)
- on pr comment /CROK (from PO mostly) : (management: move PR from in review to functionnal review), (dev: move PR from in review to functionnal review) and automatically ask review of PO ?
- on pr merged : rebase branches ? , close issue if not closed ? and move PR to Done (any project)
- on issue assigned : create branches and draft


# Interaction details
- on issue created (any installed repo) :
    - create card in management project
    - set card type according to labels (User Story, Technical Story, Task, Bug)
- on issue assigned :
    - retrieve parent issues until US/TS/Bug
    - build branches hierarchy (with issue number in it)
    - for each branch of the hierarchy, starting from highest one (TS/US/Bug) :
        - create repository dispatch with target and source branches (target = dev if branch is highest one) and issue number
        - retrieve workflow_run id when launched
        - await worflow_run end 

    - worflow of branch and draft creation should : 
        - checkout target branch
        - create source branch and checkout on it
        - create a file named remove-me-XXXXXXX.txt where XXXX are random characters
        - commit the file with a chore commit message
        - create a draft pr with source -> target branches and reference issue in body