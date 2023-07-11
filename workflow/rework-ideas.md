# Classes rework

- Organization class 
    + getProjects(orgName: string) : Project[]
    + getProjectByName(orgName: string, projectName: string) : Project

- Project class

- Repository class
    + createDispatchEvent(org: string, repo: string, eventType: string, payload: any): void

- Card class
    + createFromItem(projectId: string, item: string): Card & ProjectFields
    + updateFieldValue(projectId: string, cardId: string, fieldId: string, newValue: Object!!!!): void
    + delete(projectId: string, cardId: string)

- PullRequest class
    + getlinkedProjectCards(repo: `${string}/${string}`, prNumber: string) : (CardId & project: {id: string})[]
    + getlinkedProjectCardsWithFieldValue(repo: `${string}/${string}`, prNumber: string, fieldName: string) : (CardId & project: {id: string})[]

- Issue class
    + getParents(org: string, repo: string, issueNumber: string) : IssueWithParents