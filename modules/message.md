# **Message Module**

## **Description**
The module that will handle the display of nearly all outputs of all processes (triggerred by the user) of the IDE window

## **Features**
Format incomming logs in a generic format to have the same render aspect across the different outputs
Should store the logs history to redisplay them on frontend refresh

## **UI**
A scollable panel to show messages
a search bar to filter messages
A toggle button to show/hide the panel

## **Help**

## **Preferences**
Possibility to apply filters to messages
Possibility to search with or without regex in current messages
Possibility to change formating

## **Interactions**

### Incomming
Should listen for logs streams from other modules

### Outgoing
Should notify UI module to notify frontend that new logs arrived


## **Events**

### Listening

### Emitting