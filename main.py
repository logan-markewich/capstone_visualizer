import threading

# this shows how to create a semaphore and a thread
fileSem = threading.Semaphore()
getRssi_t = threading.Thread(target=getRssi)

def getRssi():
  fileSem.acquire()
  #insert code here
  fileSem.release()

def main():
  getRssi_t.start()

if __name__ == "__main__":
    main()
