# stuff relating to working with rssi values
import locator
import ping_n_parse

def getXY(rssi0, rssi1, rssi2):
    trilateb = locator.trilatBoy((0,0,0), (3,0,0), (1.5,3,0), 3, 1.5, 3)
    xpos, ypos = locator.trilatterate(trilateb, [rssi0, rssi1, rssi2])
    return xpos, ypos

def writeXY(rssi0, rssi1, rssi2, tagID, timestamp):
    xpos, ypos = getXY(rssi0, rssi1, rssi2)
    filename = tagID + "_vals.csv"
    with open(filename, "w") as f:
        f.write(str(timestamp) + "," + str(xpos) + "," + str(ypos) + "\n")

    f.close()
