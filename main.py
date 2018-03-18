# this is the script to run once we are ready to test.
# this script is untested and may not work
# user discretion is advised
import ping_n_parse
import visualize
import rssi
import filter

import datetime
import threading
import os
from time import sleep
from urllib.request import urlopen

# this shows how to create a semaphore and a thread
rawSem = threading.Semaphore()
valSem = threading.Semaphore()
filtSem = threading.Semaphore()

def getRssi(s_1):
    written = False
    lastLineRead = -1
    
    while(True):
        valSem.acquire()
        rawSem.acquire()
        tag = ping_n_parse.pingTag('192.168.0.12')

        ping_n_parse.csv_handler(tag)
        with open(tag.ID + "_rssi.csv", "r") as f:
            for line in f:
                line = line.strip('\n')
                fields = line.split(',')
                if(len(fields) == 4):
                    written = True
                    rssi.writeXY(int(fields[1]), int(fields[2]), int(fields[3]), tag.ID, fields[0])

        f.close()
        # os.remove('./' + tag.ID + '_rssi.csv')
        open(str(tag.ID) + '_rssi.csv', 'w').close()

        valSem.release()
        rawSem.release()
        
        valSem.acquire()
        filtSem.acquire()
        if written:
            filter.filterVals(tag.ID) # it would be nice if this name wasn't hardcoded but oh well
            # os.remove('./1234567_vals.csv')
            open('1234567_vals.csv', 'w').close()
            print("updated filtered values")
        valSem.release()
        filtSem.release()
        
        written = False
        sleep(0.05)

def vis(s_1):
    lastLineRead = -1

    sleep(10)
    while True:
        sleep(0.25)
        filtSem.acquire()
        lastLineRead = visualize.updatePlot('1234567_vals_filt.csv', lastLineRead, s_1)
        filtSem.release()

def filthyBoy():
    sleep(20000)
    while True:
        sleep(0.20)
        filtSem.acquire()
        valSem.acquire()
        filter.filterVals('1234567_vals.csv') # it would be nice if this name wasn't hardcoded but oh well
        os.remove('./1234567_vals.csv')
        open('1234567_vals.csv', 'w').close()
        valSem.release()
        filtSem.release()


def main():
  # Remove old vals file
  try:
    os.remove('./1234567_vals_filt.csv')
  except FileNotFoundError as e:
      print("Couldn't delete file that doesn't exist")
    
  # set the time on the tag
  time = str(datetime.datetime.now().time()).split(':')
  secs = int((time[2].split('.'))[0])
  secs += int(time[0])*60*60
  secs += int(time[1])*60

  secsStr = str(secs)
  while(len(secsStr) < 5):
      secsStr = "0" + secsStr

  urlopen('http://192.168.0.12/setTime/' + secsStr)
  print('Time set to ' + secsStr)
  
  s_1 = visualize.initGraph()

  s_1.open()

  sleep(5)
  
  #create threads
  getRssi_t = threading.Thread(target=getRssi, args=(s_1,))
  visualize_t = threading.Thread(target=vis, args=(s_1,))
  # filter_t = threading.Thread(target=filthyBoy)
  
  print("BE FREE MY THREADS!")
  # start threads
  getRssi_t.start()
  # filter_t.start()
  visualize_t.start()

if __name__ == "__main__":
    main()
