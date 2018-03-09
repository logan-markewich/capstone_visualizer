#Lane Larochelle
#March 8th 2018 
class RawLocation(object):
	timestamp= 0
	ESPap0= 0
	ESPap1= 0
	ESPap2= 0

	def __init__(self, timestamp, rssi0, rssi1, rssi2):
		self.timestamp= timestamp
		self.ESPap0= rssi0
		self.ESPap1= rssi1
		self.ESPap2= rssi2


class TagInfo(object):
	ID= ''
	record = []

	def __init__(self, ID, rawloc):
		self.ID=ID
		seld.record.append(rawloc)


#this should handle the pinging and parsing of a whole html response
#can't test it really until you have it hooked up.
#not sure about the class definitions needs alot of testing
def pingTag(ip):
	buffers = []
	data = urlopen('http://'+ ip +'/getTriang')
	readable = data.read().decode('utf-8')
	count=0
	for line in readable:
		if (line[:3]=='<p>' and count == 0):
			ID = line[3:len(string)-4]
			count = count +1
		elif (line[:3]=='<p>' and count > 0):
			temp = line[3:len(string)-4]
			firstgo = temp.split(': ')
			timestamp = firstgo[0]
			secondgo=firstgo.split(' ')
			for each in secondgo:
				last= each.split('=')
				if (last[0]== 'ESPap0'):
					rssi0=last[1]
				elif (last[0]== 'ESPap1'):
					rssi1 = last[1]
				elif (last[0]== 'ESPap2'):
					rssi2= last[1]

			buffers.append(info=TagInfo(ID,rawloc=RawLocation(timestamp,rssi0,rssi1,rssi2)))
	return buffers
		

string = '<p>43225: ESPap2=-33, ESPap1=-44 </p>'
papa = string[3:len(string)-4]
firstgo = papa.split(': ')
print(firstgo[0])
print(firstgo[1])
