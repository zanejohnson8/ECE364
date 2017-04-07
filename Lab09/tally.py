import operations

def getTotalDuration(eventName):
    lines = loadFile('Events.txt')
    i = 2
    length = len(lines)
    l = []
    t = []
    while i < length:
        templine = lines[i].split()
        if templine[0] == eventName:
            l.append(templine[1])
            t.append(int(templine[2]))
        i += 1
    weeks = 0
    days = 0
    hours = 0
    i = 0
    for elem in l:
        if elem[-1:] == 'w':
            weeks = elem[:-1]

        if elem[-1:] == 'd':
            days = elem[:-1]

        if elem[-1:] == 'h':
            hours = elem[:-1]
    return operations.Duration(int(weeks), int(days), int(hours))

def rankEventsByDuration(*args):
    pass


def loadFile(s):

    with open(s, "r") as signalFile:
        lines = signalFile.readlines()
    return lines

if __name__ == "__main__":
    ret = getTotalDuration('Event17')
    print(ret)