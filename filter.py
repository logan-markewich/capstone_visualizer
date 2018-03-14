import fileinput

def filterVals(filename):
    curTime = '-1'
    lastTime = '-1'
    lineNum = 0
    linesToChange = []
    with open(filename, 'r')  as f:
        data = f.readlines()
        for line in data:
            lineStr = line.strip('\n')
            fields = lineStr.split(',')
            if(fields[0] != 'NULL'):
                if(curTime == '-1'):
                    curTime = fields[0]
                else:
                    # get current and last times, to be used in future use for filtering
                    lastTime = curTime
                    curTime = fields[0]
                
                    # checki if out of bounds
                    if(int(fields[1]) > 300 or int(fields[2]) > 605 or int(fields[1]) < 0 or int(fields[2]) < 0):
                        linesToChange.append(lineNum)

            lineNum += 1
    f.close()
    
    for lineNum in linesToChange:
        data[lineNum] = 'NULL\n'

    with open(filename, 'w') as f:
        f.writelines(data)

    f.close()
            



def main():
    filterVals('1234567_val.txt')


if __name__ == "__main__":
    main()
