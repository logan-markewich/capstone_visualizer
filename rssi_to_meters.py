# use polynomial calibration funtion to convert to meters
import numpy as np

cal = [0.2254, -3.964, 24.994, -71.136, 96.131, 23.408]

def convert(rssi):
    if rssi > 0:
        return None
    cal[-1] = cal[-1] + rssi
    vals = np.roots(cal)
    #print(vals)
    while vals[-1].imag != 0:
        vals = vals[:-1]
    dist = vals[-1].real
    #print(dist)
    return dist



if __name__ == "__main__":
    import sys
    convert(int(sys.argv[1]))
