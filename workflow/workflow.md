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
