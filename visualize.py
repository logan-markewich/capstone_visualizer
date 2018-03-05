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
    stream_id2 = stream_ids[1]

    # Make instance of stream id object
    stream_1 = go.Stream(
        token=stream_id1,  # link stream id to 'token' key
        maxpoints=5      # keep a max of 5 pts on screen
    )

    stream_2 = go.Stream(
        token=stream_id2,
        maxpoints=5
    )

    # Initialize trace of streaming plot by embedding the unique stream_id
    trace1 = go.Scatter(
        x=[],
        y=[],
        mode='lines+markers',
        stream=stream_1         # (!) embed stream id, 1 per trace
    )

    # Initialize trace of streaming plot by embedding the unique stream_id
    trace2 = go.Scatter(
        x=[],
        y=[],
        mode='lines+markers',
        stream=stream_2         # (!) embed stream id, 1 per trace
    )

    data = [trace1, trace2]
    # Add title to layout object
    layout = {
        'title': 'example lample mample',
        'xaxis': {
            'range': [0,10]
        },
        'yaxis': {
            'range': [0,10]
        },
        'shapes': [
        {
            'type': 'line',
            'x0': 0,
            'y0': 0,
            'x1': 10,
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
            'y1': 10,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        {
            'type': 'line',
            'x0': 10,
            'y0': 0,
            'x1': 10,
            'y1': 10,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        {
          'type': 'line',
            'x0': 0,
            'y0': 10,
            'x1': 10,
            'y1': 10,
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
    s_2 = py.Stream(stream_id2)

    return [s_1, s_2]

def main():
    s = initGraph()

    s_1 = s[0]
    s_2 = s[1]

    s_1.open()
    s_2.open()

    time.sleep(5)

    x = -1
    y = -1
    forward = True

    while True:
        if forward:
            x += np.random.uniform(0.0,1.0)
            if x >= 10:
                x = 10

            y += np.random.uniform(0.0,1.0)
            if y >= 10:
                y = 10

            s_1.write(dict(x=x,y=y))
            s_2.write(dict(x=y,y=x))

            time.sleep(1)
            if y >= 10 or x >= 10:
                forward = False
        else:
            x -= np.random.uniform(0.0,1.0)
            if x <= 0:
                x = 0

            y -= np.random.uniform(0.0,1.0)
            if y <= 0:
                y = 0

            s_1.write(dict(x=x,y=y))
            s_2.write(dict(x=y,y=x))

            time.sleep(1)
            if y <= 0 or x <= 0:
                forward = True


if __name__ == "__main__":
    main()
