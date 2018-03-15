# this is the script to run once we are ready to test.
# this script is untested and may not work
# user discretion is advised
import ping_n_parse
import visualize
import rssi
import filter

import threading
import os
from time import sleep

# this shows how to create a semaphore and a thread
rawSem = threading.Semaphore()
valSem = threading.Semaphore()
filtSem = threading.Semaphore()

getRssi_t = threading.Thread(target=getRssi)
visualize_t = threading.Thread(target=vis)
filter_t = threading.Thread(target=filthyBoy)

def getRssi():
    while(True):
        tag = ping_n_parse.pingTag('192.168.0.12')
        rawSem.acquire()
        valSem.acquire()

        ping_n_parse.csv_handler(tag)
        with open(tag.ID + "_rssi.csv", "r") as f:
            for line in f:
                line = line.strip('\n')
                fields = line.split()
                rssi.writeXY(int(fields[1]), int(fields[2]), int(fields[3]), tag)

        f.close()
        os.remove('./' + tag.ID + '_rssi.csv')

        valSem.relase()
        rawSem.release()
        sleep(0.25)

def vis():
    s_1 = visualize.initGraph()

    s_1.open()

    sleep(5)
    lastLineRead = -1

    while True:
        sleep(0.20)
        filtSem.acquire()
        lastLineRead = visualize.updatePlot('1234567_vals_filt.csv', lastLineRead, s_1)
        filtSem.release()

def filthyBoy():
    while True:
        filtSem.acquire()
        valSem.acquire()
        filterVals('1234567_vals.csv') # it would be nice if this name wasn't hardcoded but oh well
        valSem.release()
        filtSem.release()
        sleep(0.25)

def main():
  getRssi_t.start()
  filter_t.start()
  visualize_t.start()

if __name__ == "__main__":
    main()
