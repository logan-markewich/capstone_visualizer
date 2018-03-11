import plotly.tools as tls
import plotly.graph_objs as go
import plotly.plotly as py

import time

import numpy as np

# for now this will init two trace objects(items to track)
# could be expanded using for loops
# returns stream link array, use .open() after this
def initGraph():
    # get list of all your stream ids
    stream_ids = tls.get_credentials_file()['stream_ids']

    # Get stream id from stream id list
    stream_id1 = stream_ids[0]

    # Make instance of stream id object
    stream_1 = go.Stream(
        token=stream_id1,  # link stream id to 'token' key
        maxpoints=5      # keep a max of 5 pts on screen
    )

    # Initialize trace of streaming plot by embedding the unique stream_id
    trace1 = go.Scatter(
        x=[],
        y=[],
        mode='lines+markers',
        stream=stream_1         # (!) embed stream id, 1 per trace
    )

    data = [trace1]
    # Add title to layout object
    layout = {
        'title': 'example lample mample',
        'xaxis': {
            'range': [0,300]
        },
        'yaxis': {
            'range': [0,605]
        },
        'shapes': [
        {
            'type': 'line',
            'x0': 0,
            'y0': 0,
            'x1': 300,
            'y1': 0,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        {
            'type': 'line',
            'x0': 0,
            'y0': 0,
            'x1': 0,
            'y1': 605,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        {
            'type': 'line',
            'x0': 300,
            'y0': 0,
            'x1': 300,
            'y1': 605,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        {
          'type': 'line',
            'x0': 0,
            'y0': 605,
            'x1': 300,
            'y1': 605,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        ]
    }

    # Make a figure object
    fig = {
        'data': data,
        'layout': layout
    }

    # Send fig to Plotly, initialize streaming plot, open new tab
    py.plot(fig, filename='python-streaming')

    # We will provide the stream link object the same token that's associated with the trace we wish to stream to
    s_1 = py.Stream(stream_id1)

    return s_1

def updatePlot(filename, lastLineNumRead, s):
    curLine = 0
    lastTime = -1
    x = 0
    y = 0
    with open(filename, 'r') as f:
        for line in f:
            if(line != 'NULL\n'):
                if(curLine >= lastLineNumRead):
                    line = line.strip('/n')
                    fields = line.split(',')
                    if(lastTime != -1):
                        time.sleep(int(fields[0]) - lastTime)

                    s.write(dict(x=int(fields[1]),y=int(fields[2])))
                    lastTime = int(fields[0])

                curLine += 1
    f.close()
    return curLine

def main():
    s_1 = initGraph()

    s_1.open()

    time.sleep(5)
    lastLineRead = -1

    while True:
        lastLineRead = updatePlot('1234567_fake.txt', lastLineRead, s_1)


if __name__ == "__main__":
	main()
