from urllib.request import urlopen

#Lane Larochelle
#March 8th 2018 
class RawLocation(object):
    timestamp= 0
    ESPap0= 0
    ESPap1= 0
    ESPap2= 0

    def __init__(self, timestamp, rssi0, rssi1, rssi2):
        self.timestamp = timestamp
        self.ESPap0 = rssi0
        self.ESPap1 = rssi1
        self.ESPap2 = rssi2


class TagInfo(object):
    ID = ''
    record = []

    def __init__(self, ID):
        self.ID = ID

    def addRec(self, rawloca):
        self.record.append(rawloca)

    def clearRec():
        del(record[:])

    def printInfo(self):
        print("ID: " + self.ID)
        for rec in self.record:
            print("Time:" + rec.timestamp)
            print("ESPap0: " + rec.ESPap0)
            print("ESPap1: " + rec.ESPap1)
            print("ESPap2: " + rec.ESPap2)

    def getRecords(self):
        return self.record

    def getID(self):
        return self.ID


#this should handle the pinging and parsing of a whole html response
#can't test it really until you have it hooked up.
#not sure about the class definitions needs alot of testing
def pingTag(ip):
    data = urlopen('http://'+ ip +'/getTriang')
    readable = (data.read().decode('utf-8')).split('\n')
    count = 0
    for line in readable:
        if(line[:3]=='<p>' and count == 0):
            ID = line[3:len(line)-5]
            tag = TagInfo(ID)
            count = count +1
        elif(line[:3]=='<p>' and count > 0):
            temp = line[3:len(line)-4]
            firstgo = temp.split(': ')
            timestamp = firstgo[0]
            secondgo=firstgo[1].split(' ')
            for each in secondgo:
                last = each.split('=')
                if(last[0] == 'ESPap0'):
                    rssi0 = last[1]
                elif(last[0] == 'ESPap1'):
                    rssi1 = last[1]
                elif(last[0] == 'ESPap2'):
                    rssi2 = last[1]

            tag.addRec(RawLocation(timestamp,rssi0,rssi1,rssi2))

    return tag
		

def main():
    tag = pingTag('192.168.1.166')
    tag.printInfo()

if __name__ == '__main__':
    main()
