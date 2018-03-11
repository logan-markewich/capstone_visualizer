# capstone_visualizer

******Before running anything, make sure plotly and numpy is installed, and that you have set up your plotly credentials and api keys correctly

Alright, things we need (or possibly need):
- A way to organize what rssi belongs to which tag id(DONE!)
- A function that fetches data from all tags?(DONE!)
    ** This is pretty much done you just need to pass the function the ip of the tag you want to ping
- A function to convert RSSI -> cm
- A function to write the information to a file or something? Need to think of how to store the data.. maybe each tag gets a csv(DONE!)
- A function to go through the newest data and filter out data where a pigs appears to move way to far way to fast, or is out of the room(DONE! but only for out of bounds locations)
- A function to stream/update the plotly graph (I would only worry about a single point right now)(HALF WAY DONE)
    - As a side note, all graph settings (looks, etc) can be updated in the plotly website
    - Also, we can draw shapes to represent the room we give the presentation in, or a pig pen, right on the graph
    

We should probably start with getting a graph streaming with some fake data, then we can figure out how to convert and filter values.

You'll need a plotly account to get the api key and streaming keys.

# Current Status
The visualize.py file will now generate a plot with two traces, that move randomly, on a plot that has walls drawn on it. The plot is live streamed to the associated plotly account on your computer.

Ping n Parse will ping a tag, and get the RSSI values and timestamps from it's buffer. It also has a function that takes everything in the tag objects record and writes it to a csv file, and then clears the tag record for memory svaing.

# Next Steps
- Change visualizer to read in from a stock text file(csv? one fore each tag?)
- use RSSI values to get a function/trendline that works
- formulate main.py to get everything working in tandem

# Far off goals
- format the plot to look nicer, have extra titles and whatnot
- make plotted points large enough to account for error in location


