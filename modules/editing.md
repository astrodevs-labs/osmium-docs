# **Editing Module**

## **Description**
This module will be in charge of the code edition the user will perform on all files

## **Features**
Should store the paths of all openned files
Should retain the focused file tab for next reopens
Should save file when requested to
Should retain if tab is temporary or persistent ? 

## **UI**
Tabs for each opened folder
Display file content in each tab
Modify file content when keypad is is stroke

## **Help**

## **Preferences**
Font size
Max opened tabs
Effect of double click (temporary/persitent tab ?)
Show/Hide line numbers
Show/Hide white spaces
Line-wrapping settings
Code-wrapping settings ? (default behavior or specific with project types/languages ?) 
## **Interactions**

### Incomming
Listen for file content edition (from UI module)
Listen for file content change (from file watcher)

### Outgoing
Notify frontend in case of file content change 

## **Events**

### Listening

### Emitting