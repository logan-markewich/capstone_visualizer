# this is the script to run once we are ready to test.
# this script is untested and may not work
# user discretion is advised
import ping_n_parse
import visualize
import rssi
import filter

import threading

# this shows how to create a semaphore and a thread
rawSem = threading.Semaphore()
valSem = threading.Semaphore()
filtSem = threading.Semaphore()

getRssi_t = threading.Thread(target=getRssi)
visualize_t = threading.Thread(target=vis)
locate_t = threading.Thread(target=locate)
filter_t = threading.Thread(target=filthyBoy)

def getRssi():
    while(True):
        sleep(0.25)
        tag = ping_n_parse.pingTag('192.168.0.12')
        rawSem.acquire()
        ping_n_parse.csv_handler(tag)
        rawSem.release()

def locate():
    # this needs to use locater, should probably also write location data to
    # file somehow, gaurded by semaphore. Should be one file for RSSI vals
    # and another file for location vals
    while True:
        sleep(0.30)
        rawSem.acquire()
        valSem.acquire()
        rssi.writeXY(?)
        valSem.release()
        rawSem.release()

def vis():
    s_1 = visualize.initGraph()

    s_1.open()

    time.sleep(5)
    lastLineRead = -1

    while True:
        filtSem.acquire()
        lastLineRead = visualize.updatePlot('1234567_vals_filt.txt', lastLineRead, s_1)    
        filtSem.release()
        sleep(0.20)


def filthyBoy():
    while True:
        filtSem.acquire()
        valSem.acquire()
        filterVals('1234567_vals.txt')
        valSem.release()
        filtSem.release()
        sleep(0.25)

def main():
  getRssi_t.start()
  locate_t.start()
  filter_t.start()
  visualize_t.start()

if __name__ == "__main__":
    main()
