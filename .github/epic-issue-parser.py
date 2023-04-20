import json
import os
import re
import requests

def create_subissue(parent_issue_number, sub_issue_title):
    org = os.environ["GITHUB_ORGANIZATION"]
    repo = os.environ["GITHUB_REPOSITORY"]
    token = os.environ["GITHUB_TOKEN"]
    # create a new sub-issue using the GitHub API
    url = f"https://api.github.com/repos/{org}/{repo}/issues"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "title": sub_issue_title,
        "labels": ["task"],
        "assignees": []
    }
    data["issue"] = parent_issue_number
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 201:
        print(f"Failed to create sub-issue: {response.content}")
    else:
        sub_issue_number = response.json()["number"]
        return sub_issue_number

def update_parent_issue(parent_issue_number, checkbox_text, sub_issue_number, issue_body):
    org = os.environ["GITHUB_ORGANIZATION"]
    repo = os.environ["GITHUB_REPOSITORY"]
    token = os.environ["GITHUB_TOKEN"]
    # update the parent issue with the sub-issue number
    url = f"https://api.github.com/repos/{org}/{repo}/issues/{parent_issue_number}"
    headers = {"Authorization": f"Bearer {token}"}
    issue_body = re.sub(f"- \\[ \\] {re.escape(checkbox_text)}", f"- [ ] {checkbox_text} ([#{sub_issue_number}])", issue_body)
    data = {
        "body": issue_body
    }
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Failed to update parent issue: {response.content}")
    return issue_body

def main(event_payload):
    # extract relevant data from the webhook payload
    parent_issue_number = event_payload["issue"]["number"]
    issue_body = event_payload["issue"]["body"]
    parent_issue_labels = event_payload["issue"]["labels"]
    
    # check if the parent issue has the "epic" label
    parent_issue_is_epic = False
    for label in parent_issue_labels:
        if label["name"] == "epic":
            parent_issue_is_epic 

    if not parent_issue_is_epic:
        return
    
    # extract checkboxes from the issue body
    checkboxes = []
    for line in issue_body.splitlines():
        match = re.match(r"- \[( |x)\] (.+?)($|\s+\[#\d+\])", line)
        if match:
            checkbox_text = match.group(2)
            checkbox_checked = match.group(1) == "x"
            checkbox_sub_issue_number = None
            if match.group(3):
                checkbox_sub_issue_number = int(re.search(r"#(\d+)", match.group(3)).group(1))
            checkboxes.append((checkbox_text, checkbox_checked, checkbox_sub_issue_number))
    
    # create sub-issues for each checked checkbox (if the parent issue is not an epic)
    for checkbox_text, checkbox_checked, checkbox_sub_issue_number in checkboxes:
        if not parent_issue_is_epic and checkbox_checked and not checkbox_sub_issue_number:
            sub_issue_title = checkbox_text
            sub_issue_number = create_subissue(parent_issue_number, sub_issue_title)
            if sub_issue_number:
                issue_body = update_parent_issue(parent_issue_number, checkbox_text, sub_issue_number, issue_body)
        
if __name__ == "__main__":
    event_payload = json.loads(open(os.environ["GITHUB_EVENT_PATH"]).read())
    main(event_payload)
