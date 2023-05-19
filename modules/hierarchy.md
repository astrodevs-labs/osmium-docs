# **Hierarchy Module**

## **Description**

This module is responsible for showing the current hierarchy of files and directories of a project.

## **Features**

- Get the current files inside the project
- Associate file types with corresponding icon
- Typing folders depending on project type or even default settings
## **UI**

- File Tree with collapsable folders
- Different views to hide some files

## **Help**

## **Preferences**

## **Interactions**

### Incomming

- Events of file watcher from file module in case of external IDE changes

### Outgoing

- Send file/folder manipulation (beside file edition) events to the file module (to operate the corresponding filesystem changes)

## **Events**

### Listening

### Emitting