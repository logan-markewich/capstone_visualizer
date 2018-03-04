# capstone_visualizer

Alright, things we need (or possibly need):
- A way to organize what rssi belongs to which tag id
- A function that fetches data from all tags?
- A function to convert RSSI -> meters/cm/idk
- A function to write the information to a file or something? Need to think of how to store the data.. maybe each tag gets a csv
- A function to go through the newest data and filter out data where a pigs appears to move way to far way to fast, or is out of the room
- A function to stream/update the plotly graph (I would only worry about a single point right now)
    - As a side note, all graph settings (looks, etc) can be updated in the plotly website
    - Also, we can draw shapes to represent the room we give the presentation in, or a pig pen, right on the graph
    

We should probably start with getting a graph streaming with some fake data, then we can figure out how to convert and filter values.

You'll need a plotly account to get the api key and streaming keys.
