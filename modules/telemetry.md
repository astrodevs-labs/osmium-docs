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
- A window pop-up with crashes informations and a form to add custom additional informations

## **Help**

## **Preferences**

## **Interactions**

### Incomming

- Should listen for multiples telemetry events requests from other modules
- Should listen for UI module see if checkbox has been clicked or not
- Should listen for UI module see if crash form has been submitted

### Outgoing

- Should notify UI module to notify frontend that the consent form needs to be shown
- SHould notify UI module to notify frontend that the crash form needs to be shown

## **Events**

### Listening

### Emitting