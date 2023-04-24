# **Frontend Communication Module**

## **Description**
This module will provide an abstraction of the network frontedn-backend protocole. It will be the entrypoint of all frontend requests in the backend and the module that will emit event to the frontend on behalf of other modules.

## **Features**
- Maintain an active bidirectional connection with the frontend (server)
- Handle request from the frontend and buffer them until there is a response of all concerned modules
- Emit event to the frontend

## **UI**

## **Help**

## **Preferences**
- Authentication method
- Number of allowed clients to connect
- Port of server

## **Interactions**

### Incomming
- Events to emit to the frontend from UI module

### Outgoing
- All requests from the frontend to the UI module


## **Events**

### Listening

### Emitting