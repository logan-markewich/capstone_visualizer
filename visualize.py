import plotly.tools as tls
import plotly.graph_objs as go
import plotly.plotly as py

import time

# for now this will init one trace object(item to track)
# could be expanded using for loops
# returns stream link, use .open() after this
def initGraph():
  # get list of all your stream ids
  stream_ids = tls.get_credentials_file()['stream_ids']
  
  # Get stream id from stream id list 
  stream_id = stream_ids[0]

  # Make instance of stream id object 
  stream_1 = go.Stream(
    token=stream_id,  # link stream id to 'token' key
    maxpoints=5      # keep a max of 5 pts on screen
  )
  
  # Initialize trace of streaming plot by embedding the unique stream_id
  trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream_1         # (!) embed stream id, 1 per trace
  )

  data = go.Data([trace1])
  # Add title to layout object
  layout = go.Layout(title='Sample example mample')

  # Make a figure object
  fig = go.Figure(data=data, layout=layout)

  # Send fig to Plotly, initialize streaming plot, open new tab
  py.plot(fig, filename='python-streaming')
  
  # We will provide the stream link object the same token that's associated with the trace we wish to stream to
  return py.Stream(stream_id)

def main():
  s = initGraph()
  
  time.sleep(5)
  
  x = -1
  y = -1
  forward = True
  
  while True:
    if forward:
      x += 0.25
      y += 0.5
      
      s.write(dict(x=x,y=y)
      
      time.sleep(1)
      if y > 6:
              forward = False
    else:
      x -= 0.25
      y -= 0.5
      
      s.write(dict(x=x,y=y)
      
      time.sleep(1)
      if y <= -1:
              forward = True


if __name__ == "__main__":
  main()
  
  
