# **Telemetry Module**

## **Description**

This module is responsible for gathering informations about crash and possible bugs within the app to then transmit them to us.

## **Features**

- Store crashs informations
- Generate crash reports
- Send telemtry reports to open telemetry server

## **UI**

- Consent form at the start of the IDE:
    - A checkbox to allow or not
    - A text saying that the loegal stuff

## **Help**

## **Preferences**

## **Interactions**

### Incomming
Should listen for multiples telemetry events requests from other modules
Should listen for UI module see if checkbox has been clicked or not

### Outgoing
Should notify UI module to notify frontend that the consent form needs to be shown
## **Events**

### Listening

### Emitting