# **Module**

This file aims to list the different processes in the IDE categorized by Module.

## **Build Module**

### Build button pressed:
- Generated event by front when clicking on the build button (lets say id = build)
- UI Module: emits the event: 'build' button pressed
- Build Module recognize this event because its UI layer registered the button with this id.
- Build Module emits a first event to fetch needed ressources to make a build.
- Preferences/Configuration/Filesystem modules received this event and fills the payload with the nessecary ressources.
- Since this event was awaited by the Build Module, it now emits an event with theses informations to the LSP module by targeting a Blockchain Plugin.
- LSP Module recognize a LSP Payload, it translates it and emits an event for the Plugin Module
- The Plugin Module emits an LSP event to all Plugins in the hope that somme plugins will handle this event.
- The corresponding Blockchain Plugin recognized this event and is now proccessing to the build with the passed data.
- It is starting to emmit events corresponding to logs and build steps to the Plugin Module.
- The Plugin Module emits an event that only the LSP Module know about. It translates its data and makes a payload.
- The LSP service emmits events that are listened by the Message Module wich it-self emmits UI Payloads to show the logs.
- The Build Module may recognize also some events concerning the builds steps to updated the corresponding UI.


## **Editing Module**

### Focusing on code editor:
- Generated event by front when clicking on a window file (lets say id = my-file)
- The Editing Module recognized this event because it stores all the opened files.
- It sets this file as the actual focused file and places the cursor on the file correctly.
- It generates an UI event to update the corresponding UI states.
- The UI Module recognized this UI state update and translates it to send updates to the Front.

### Pressing on a Key: (May involve state verification to check if this event is to be handled by the Editing Module (file window focused))
### Selecting Code (May involve continuous events with the fact that the mouse button is held down in the process):


## **Configuration Module**

### Configuration tab button pressed:
### New configuration pressed:
### Selected configuration:
### Configuration "field" Input (may need to differienciate regular fields and typed fields such as filepaths):
### Configuration "dropdown" clicked:


## **Deploy Module**

### Opened Deploy Configuration Tab:
### Deploy networks "dropdown" clicked:
### Selected network:
### Pressed on new local network:
Need to describe various deploy event types (success, deployement infos, storing sc address, failure and messages, etc ...)


## **Help Module**
Need to list global help functionnalities.


## **Debug Module**

### Pressed on bottom "debug" window tool button:
### Pressed on top left "run debug" button:
Need to describe various configuration and live debbuging events in the bottom tool window


## **Tests Module**

### Run currently selected tests config:
### Specific test clicked:


## **Preference Module**

Need to list all preferences sub-categories events:
- short cuts
- plugins
- themes
- preferences for all other services functionnalities ...



## **Short Cuts Module**

### Pressed on bottom shortcut button:
### Pressed a shortcut to update:


## **History service**
Need to list type of actions to save in history.


## **File Module**

### Create a new file button pressed:
### Rename a file button pressed:
### Create a directory button pressed:
### Remove a file / directory button pressed:
### Opened a file:
### Closed a file:
### Splited a file:


## **Projects Module**

### Opened a project:
### Creating a project:
### Save the project:
### Clicked on 'Open recent project' sub-menu in 'file' menu in toolbar


## **Filesystem Module** 
Need to discuss about the purpose of this service

### New file to watch:
### File edited:


## **LSP Module**
## **UI Module**


## **Plugin Module**
Listen to moslty any events emmited by other micro-services.


## **Terminal Module**

Need to list all options modifying events of the terminal tool window

### Split terminal button pressed:
### Create a new terminal window button pressed:
### Change shell button pressed:


## **Messages Module**
Need to list all log types, traces and their origins


## **Notifications Module**

### New IDE notification to show on bottom right footer:
### New Plugin notification to show on bottom right footer:


## **Git Module**

### Commit button button pressed:
### Add a file to stage button pressed:
### Remove a file from stages button pressed:
### New branch button pressed:
### Create a new PR / MR button pressed (depends on github / gitlab):
### Show git commits history button pressed:


## **TODO Module**

### Check TODO on file change:
Need to describe TODO tool window filtering configuration


## **Interacting Module**

### Pressed on open/close Interacting tab:
### Focusing on 'array' field type in interacting tab:
### Pressed on 'add wallet' button for wallet field type in interacting tab:
### Pressed on 'add interaction to chain' button in interacting tab
### Pressed on execute button:
Need to describe caller configuration modifications events

## **Problems Module**

### Code diagnostic problem emitted from file editing:
### Code diagnostic problem emitted from openning a project:
### Pressed on "diagnose" button in Problem tool window:
Need to describe filtering options modifitactions events


## **Logging Module**


## **Telemetry Module**

