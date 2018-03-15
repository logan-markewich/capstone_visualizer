# stuff relating to working with rssi values
import locator
import ping_n_parse

def getXY(rssi0, rssi1, rssi2):
    trilateb = locator.trilatBoy()
    xpos, ypos = trilatterate(trilatebboy, [rssi0, rssi1, rssi2]):
    return xpos, ypos

def writeXY(rssi0, rssi1, rssi2, tag):
    xpos, ypos = getXY(rssi0, rssi1, rssi2)
    with open(tag.ID + "vals.txt", "w") as f:
        f.write(tag.timeStamp + "," + xpos + "," + ypos + "\n")
    
    f.close()
        
  
  
