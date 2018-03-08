# capstone_visualizer

******Before running anything, make sure plotly and numpy is installed, and that you have set up your plotly credentials and api keys correctly

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

# Current Status
The visualize.py file will now generate a plot with two traces, that move randomly, on a plot that has walls drawn on it. The plot is live streamed to the associated plotly account on your computer.

# Next Steps
- Change visualizer to read in from a stock text file(csv? one fore each tag?)
- Create function to randomly populate a text file (text file should be gaurded by semaphore, we will need threading)
- Work on parsing response from ESP's and figuring out the temp storage for those values before they get deposited into text file (some kind of queue/dictionary ??)

# Far off goals
- format the plot to look nicer, have extra titles and whatnot
- make plotted points large enough to account for error in location


