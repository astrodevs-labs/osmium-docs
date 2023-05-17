# US 1 - Open/Read a file
### 'Component(s)' == front react component + module component

## Launch the IDE binary starts the application
- [ ] Create a tauri project with the tauri cli
- [ ] Add react to the tauri project
- [ ] Add a script to bundle backend and frontend into one binary


## During startup, the frontend launches the backend process
- [ ] Create a buildable binary for the back end process
- [ ] Add it in an accessible build folder for the client
- [ ] Execute the backend binary from the client at startup


## The frontend initiate websocket connection to the backend and perform handshake
- [ ] Initialize frontend protocol client with the backend address/port
- [ ] send initial handshake message to the backend
- [ ] register new client as frontend in the backend
    

## The frontend requests the layout to display through a graphql query created by the protocol client
- [ ] Create a graphql query to get the layout
- [ ] Send the graphql query to the backend using the protocol client


## The frontend-communication module handles the layout request and emit a layoutPayload event
- [ ] Create a layoutPayload event
- [ ] Emit the layoutPayload event when the layout request is received


## The backend responds with first visual layout
- [ ] Create the empty UIModule
- [ ] Create the empty LayoutModule
- [ ] Create the ComponentPayload 
- [ ] Add static method to create 'left-side-bar' ComponentPayload
- [ ] Add static method to create 'center-canvas' ComponentPayload
- [ ] Create the NewLayoutPayload
- [ ] Register empty handler for NewLayoutPayload - LayoutModule
- [ ] Add 'left side bar' and 'center-canvas' to NewLayoutPayload - LayoutModule
- [ ] Register empty handler for NewLayoutPayload - UIModule
- [ ] Add the new components in the tree - UIModule
- [ ] Use the data of NewLayoutPayload to generate GraphQL response - FrontComModule


## The user can see a visual layout in the window
### Front end
- [ ] Create an empty recursive factory pattern to generate components based on GraphQL response
- [ ] Create the generic 'root-component' and its factory builder
- [ ] Create the generic 'side-bar' component and its factory builder
- [ ] Create the generic 'center-canvas' component and its factory builder
- [ ] Call the factory to generate the new react tree


## The user can see a view port when clicking on hierarchy button
### Back end
- [ ] Create the empty HierarchyModule
- [ ] Add static method to create 'expendable-list-view' ComponentPayload
- [ ] Add static method to create 'button' ComponentPayload
- [ ] Add static method to create 'icon-button' ComponentPayload
- [ ] Register empty handler for the NewLayoutPayload - HierarchyModule
- [ ] Add a condition for the handler if the NewLayoutPayload root component is 'editor' - HierarchyModule
- [ ] Add 'icon-button' to the 'left-side-bar' in NewLayoutPayload - HierarchyModule
- [ ] Register empty handler on click of the 'icon-button' in sidebar - HierarchyModule
- [ ] Attach/Remove 'expendable-view-list' to 'left-side-bar' when Hierarchy button clicked
### Front end
- [ ] Create 'expendable-list-view' component and factory builder
- [ ] Create 'side-bar-view-port' component and factory builder
- [ ] Create 'button' component and factory builder
- [ ] Create 'icon-button' component and factory builder
- [ ] Add 'hierarchy-icon' in assets


## The user can see a centered tabs manager
- [ ] Create the empty TabsModule
- [ ] Add static method to create 'tabs-manager' ComponentPayload
- [ ] Add static method to create generic 'tab' ComponentPayload
- [ ] Register empty handler for the NewLayoutPayload - TabsModule
- [ ] Add a condition for the handler if the NewLayoutPayload root component is 'editor' - TabsModule
- [ ] Add 'tabs-manager' in the 'center-canvas' in the NewLayoutPayload - TabsModule
- [ ] Register empty handler for the NewTabPayload - TabsModule
- [ ] Create a tab component on NewTabPayload - TabsModule
- [ ] Emit a ComponentTreeUpdate on new tab received - TabsModule


## The back end generates the tree view of files
### Back end
- [ ] Create the empty FileModule
- [ ] Add static method to create 'simple-icon' ComponentPayload
- [ ] Add static method to create 'label' ComponentPayload
- [ ] Add static method to create 'card' ComponentPayload
- [ ] Add method to retrieve file/directory tree from input directory
- [ ] Emit a async ProjectFilesPayload when NewLayoutPayload received with 'editor' root component - FileModule
- [ ] Register empty handler on ProjectFilesPayload - HierarchyModule
- [ ] Add method to create a 'directory-card' ComponentPayload
- [ ] Add method to create a 'file-card' ComponentPayload
- [ ] Emit a async ComponentTreeUpdate to update the hierarchy - HierarchyModule


## The user can navigate in his directory with the hierarchy view port
(related component ui modules) + UI Module + FrontCom module == ComponentTreePayload && front component update handling
### Back End
- [ ] Register empty handler on ComponentTreePayload - UIModule
- [ ] Update internal component tree - UIModule
- [ ] Create GraphQL event on ComponentTreePayload - FrontComModule
- [ ] Send GraphQL ComponentTreeUpdate event to front - FrontComModule

### Front End
- [ ] Create 'icon' component and factory builder
- [ ] Create 'label' component and factory builder
- [ ] Create 'card' component and factory builder


## The user can select a file entry in the hierarchy view port
### Front End
- [ ] Register a handler for click on a file item component
- [ ] Use protocol client to build a "button clicked" event
- [ ] Send the event to the backend


## The backend sends the file content to the frontend
### Back End
- [ ] Create empty EditingModule
- [ ] Register empty handler on ComponentStateEvent: 'file entry: button clicked' - HierarchyModule
- [ ] Emit async OpenFileEvent with filepath - HierarchyModule.
- [ ] Register empty handler on OpenFileEvent - EditingModule
- [ ] Add static method to create 'file-tab' ComponentPayload
- [ ] Emit event NewTabModule with new file tab - EditingModule
- [ ] Register the result of NewTabModule - EditingModule
- [ ] Emit event ReadFileEvent - EditingModule
- [ ] Register empty handler on ReadFileEvent - FileModule
- [ ] Create a method to read a file content - FileModule
- [ ] Create a method to encode in base64 any file content - FileModule
- [ ] Add file content to ReadFileEvent payload - FileModule
- [ ] Emit ComponentTreeUpdate with file content of ReadFileEvent - EditingModule



## The user should be able to see the file content in a file tab
### Front End
- [ ] Create 'file-tab' component and factory builder
- [ ] Make a hook to decode the file content received in the 'file-tab' component
Need further investigations.

 
