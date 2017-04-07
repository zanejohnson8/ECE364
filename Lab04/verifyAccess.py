
def getUserPermissions():
    cardsFile = loadFile("./AccessCards.txt")
    IDdict = dict()
    ret = dict()
    acc = set()
    length = len(cardsFile)
    i = 2
    while (i < length - 1):
            tempLine = cardsFile[i].split()
            temp_s0 = str(tempLine[0] + " " + tempLine[1])
            temp_s1 = str(tempLine[3])
            IDdict.update({temp_s0:temp_s1})
            ret.update({temp_s0:acc})
            i += 1
    rev = dict((v,k) for k,v in IDdict.items())
    perm = loadFile("./Permissions.txt")
    length = len(perm)
    permDict = dict()
    prevID = str()
    i = 2
    tempset = set()
    while (i < length):

        tempLine = perm[i].split()
        temp_s0 = tempLine[0]
        if (temp_s0 != prevID):
            tempset = set()
        temp_s1 = str(tempLine[2])
        permDict.update({temp_s0:temp_s1})
        name = rev[temp_s0]
        tempset.add(temp_s1)
        ret[name] = tempset
        prevID = temp_s0
        i += 1
    pass
    return ret

def getFloorPermissions():
    pass
    cardsFile = loadFile("./AccessCards.txt")
    IDdict = dict()
    ret = dict()
    acc = set()
    length = len(cardsFile)
    i = 2
    while (i < length - 1):
            tempLine = cardsFile[i].split()
            temp_s0 = str(tempLine[0] + " " + tempLine[1])
            temp_s1 = str(tempLine[3])
            IDdict.update({temp_s0:temp_s1})
            ret.update({temp_s0:acc})
            i += 1
    rev = dict((v,k) for k,v in IDdict.items())
    perm = loadFile("./Permissions.txt")
    length = len(perm)
    permDict = dict()
    acc = set()
    i = 2
    tempset = set()
    while (i < length):
        tempLine = perm[i].split()
        temp_s0 = tempLine[2]
        temp_s1 = str(tempLine[0])
        permDict.update({temp_s0:set()})
        i += 1
    i = 2
    while (i < length):
        tempLine = perm[i].split()
        temp_s1 = str(tempLine[0])
        temp_s0 = tempLine[2]
        tempset = permDict[temp_s0]
        tempset.add(rev[temp_s1])
        permDict.update({temp_s0:tempset})
        i += 1
    return (permDict)
def getFloorRooms():
    pass
    log = loadFile("./AccessLog.txt")
    length = len(log)
    i = 0
    logDict = dict()
    while (i < length):
        tempLine = log[i].split()
        temp_s0 = tempLine[2]
        temp_s1 = temp_s0.split('-')
        logDict.update({temp_s1[0]:set()})
        i += 1
    i = 0
    while (i < length):
        tempLine = log[i].split()
        temp_s0 = tempLine[2]
        temp_s1 = temp_s0.split('-')
        tempset = logDict[temp_s1[0]]
        tempset.add(temp_s1[1])
        logDict[temp_s1[0]] = tempset
        i += 1
    return (logDict)


def isAccessGrantedFor(userName, attempt):
    pass
    Userperm = getUserPermissions()
    floorRoomdict = getFloorRooms()
    floorset = Userperm[userName]
    floor = attempt[0]
    room = attempt[1]
    for x in floorset:
            if (str(x) == floor):
                b = bool(True)
                s1 = floorRoomdict[floor]
                for y in s1:
                    if (str(y) == room):
                        b = bool(True)
                        break
                    else:
                        b = bool(False)
                break
            else:
                b = bool(False)
    return(b)




def checkAttempts():
    pass
    cardsFile = loadFile("./AccessCards.txt")
    IDdict = dict()
    ret = dict()
    acc = set()
    length = len(cardsFile)
    i = 2
    while (i < length - 1):
            tempLine = cardsFile[i].split()
            temp_s0 = str(tempLine[0] + " " + tempLine[1])
            temp_s1 = str(tempLine[3])
            IDdict.update({temp_s0:temp_s1})
            ret.update({temp_s0:acc})
            i += 1
    Userdict = dict((v,k) for k,v in IDdict.items())
    log = loadFile("./AccessLog.txt")
    length = len(log)
    l = []
    i = 0
    b = bool(True)
    s = set()
    nameFloordict = getUserPermissions()
    floorRoomdict = getFloorRooms()
    while (i < length):
        tempLine = log[i].split()
        ID = tempLine[0]
        user = Userdict[ID]
        temp_s0 = tempLine[2]
        temp_s1 = temp_s0.split('-')
        room = temp_s1[1]
        floor = temp_s1[0]
        s = nameFloordict[user]
        for x in s:
            if (str(x) == floor):
                b = bool(True)
                s1 = floorRoomdict[floor]
                for y in s1:
                    if (str(y) == room):
                        b = bool(True)
                        break
                    else:
                        b = bool(False)
                break
            else:
                b = bool(False)

        A = (user, floor, room, b)
        l.append(A)

        i += 1
    return(l)
    perm = loadFile("./Permissions.txt")
    length = len(perm)
    permDict = dict()
    acc = set()
    i = 2
    tempset = set()
    while (i < length):
        tempLine = perm[i].split()
        temp_s0 = tempLine[2]
        temp_s1 = str(tempLine[0])
        permDict.update({temp_s0:set()})
        i += 1
    i = 2
    while (i < length):
        tempLine = perm[i].split()
        temp_s1 = str(tempLine[0])
        temp_s0 = tempLine[2]
        tempset = permDict[temp_s0]
        tempset.add(rev[temp_s1])
        permDict.update({temp_s0:tempset})
        i += 1

def getAttemptsOf(userName):
    pass
    l = checkAttempts()
    length = len(l)
    i = 0
    ret = []
    while (i < length):
        if (str(l[i][0]) == userName):
            A = (l[i][1], l[i][2], l[i][3])
            ret.append(A)
        i += 1
    ret1 = list(ret)
    ret1.sort()
    return(ret1)


def getUserAttemptSummary():
    pass
    cardsFile = loadFile("./AccessCards.txt")
    ret = dict()
    length = len(cardsFile)
    i = 2
    while (i < length - 1):
            tempcor = 0
            tempwro = 0
            tempLine = cardsFile[i].split()
            temp_s0 = str(tempLine[0] + " " + tempLine[1])
            l = getAttemptsOf(temp_s0)
            for x in l:
                if (x[2] == True):
                    tempcor += 1
                else:
                    tempwro += 1
            t = (tempcor, tempwro)
            ret.update({temp_s0 : t})
            i += 1
    return (ret)


def getFloorAttemptSummary():
    pass
    perm = loadFile("./Permissions.txt")
    length = len(perm)
    permDict = dict()
    l = checkAttempts()
    i = 2
    k = 0
    length1 = len(l)
    while (i < length):
        tempcor = 0
        tempwro = 0
        tempLine = perm[i].split()
        temp_s0 = tempLine[2]
        while (k < length1):
                if (l[k][1] == temp_s0):
                        if (l[k][3] == True):
                                tempcor += 1
                        else:
                                tempwro += 1
                k += 1
        k = 0
        A = (tempcor, tempwro)
        permDict.update({temp_s0:A})
        i += 1
    return (permDict)

def getRoomAttemptSummary():
    pass

def loadFile(file):

    with open(file, "r") as signalFile:
        lines = signalFile.readlines()
    return lines


if __name__ == "__main__":
    ret = getUserPermissions()
    print(ret)
    ret = getFloorPermissions()
    print(ret)
    ret = getFloorRooms()
    print(ret)
    ret = checkAttempts()
    print(ret)
    ret = isAccessGrantedFor('Reed, Bobby', ('Equipments', 'Room46'))
    print(ret)
    ret = getAttemptsOf("Gray, Tammy")
    print(ret)
    ret = getUserAttemptSummary()
    print(ret)
    print(ret["Price, Dorothy"])
    ret = getFloorAttemptSummary()
    print(ret)
    print(ret['Chemicals'])
