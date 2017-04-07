import re
from uuid import UUID

def getRejectedEntries():
    ret = list()
    lines = loadFile("./CompanyEmployees.txt")
    cnt = 0
    for l in lines:
        name = findNAME(l)
        uuid = findUUID(l)
        if (uuid == 0):
            cnt += 1
        phone = findPHONE(l)
        if (phone == 0):
            cnt += 1
        state = findSTATE(l)
        if (state == 0):
            cnt += 1
        if (cnt == 3):
            ret.append(str(name))
        cnt = 0

    return sorted(ret)
def findNAME(line):
    expr = r"(?P<name>\w+,? \w+)"
    match = re.search(expr, line, re.I)
    if (match):
        name = match.group("name")
        l = re.findall(r"\w+|\S+", name)
        if (l[1] == ','):
            name = l[2] + ' ' + l[0]
        return name
    else:
        name =  0
        return name

def findUUID(line):
    expr = r"[, ;]*(?P<uuid>{?[0-9a-fA-F]{8}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{12}}?)"
    match = re.search(expr, line, re.I)
    if (match):
        uuid = match.group("uuid")
        uuid = str(UUID(uuid))
        return uuid
    else:
        uuid = 0
        return uuid

def findPHONE(line):
    expr = r"[, ;]*(?P<phone>[(]?\d{3}[)]?[ -]?\d{3}-?\d{4})"
    match = re.search(expr, line, re.I)
    if (match):
        phone = match.group("phone")
        l = re.findall(r"\w+|\S+", phone)
        expr = r"[(][\d+)]"
        m = re.search(expr, l[0])
        if (m):
            x = 1
        else:
            length = len(l)
            if (length == 1):
                l0 = l[0]
                phone = '(' + str(l0[0:3]) + ') ' + str(l0[3:6]) + '-' + str(l0[6:10])
            elif (length == 2):
                l1 = l[1]
                phone = '(' + str(l[0]) + ') ' + str(l1[1:])
        return phone
    else:
        phone =  0
        return phone
def findSTATE(line):
    expr = r"[, ;]*(?P<state>[\w ]+\n$)"
    match = re.search(expr, line, re.I)
    if (match):
        state = match.group("state")
        length = len(state)
        return state[:length - 1]
    else:
        state = 0
        return state


def getCompleteEntries():
    ret = dict()
    lines = loadFile("./CompanyEmployees.txt")
    cnt = 0
    for l in lines:
        name = findNAME(l)
        uuid = findUUID(l)
        if (uuid == 0):
            cnt += 1
        phone = findPHONE(l)
        if (phone == 0):
            cnt += 1
        state = findSTATE(l)
        if (state == 0):
            cnt += 1
        if (cnt == 0):
            ret.update({name:(uuid, phone, state)})
        cnt = 0

    return ret


def getEmployeesWithIDs():
    ret = dict()
    lines = loadFile("./CompanyEmployees.txt")
    for l in lines:
        name = findNAME(l)
        uuid = findUUID(l)
        if (uuid != 0):
            ret.update({name:uuid})
    return ret




def getEmployeesWithPhones():
    ret = dict()
    lines = loadFile("./CompanyEmployees.txt")
    for l in lines:
        name = findNAME(l)
        phone = findPHONE(l)
        if (phone != 0):
            ret.update({name:phone})
    return ret


def getEmployeesWithStates():
    ret = dict()
    lines = loadFile("./CompanyEmployees.txt")
    for l in lines:
        name = findNAME(l)
        state = findSTATE(l)
        if (state != 0):
            ret.update({name:state})
    return ret


def getEmployeesWithoutIDs():
    ret = list()
    lines = loadFile("./CompanyEmployees.txt")
    rej = getRejectedEntries()
    chk = 0
    for l in lines:
        name = findNAME(l)
        uuid = findUUID(l)
        if (uuid == 0):
            for n in rej:
                if (name == n):
                    chk += 1
            if (chk < 1):
                ret.append(name)
        chk = 0

    return sorted(ret)


def getEmployeesWithoutPhones():
    ret = list()
    lines = loadFile("./CompanyEmployees.txt")
    rej = getRejectedEntries()
    chk = 0
    for l in lines:
        name = findNAME(l)
        phone = findPHONE(l)
        if (phone == 0):
            for n in rej:
                if (name == n):
                    chk += 1
            if (chk < 1):
                ret.append(name)
        chk = 0

    return sorted(ret)


def getEmployeesWithoutStates():
    ret = list()
    lines = loadFile("./CompanyEmployees.txt")
    rej = getRejectedEntries()
    chk = 0
    for l in lines:
        name = findNAME(l)
        state = findSTATE(l)
        if (state == 0):
            for n in rej:
                if (name == n):
                    chk += 1
            if (chk < 1):
                ret.append(name)
        chk = 0

    return sorted(ret)

def loadFile(s):

    with open(s, "r") as signalFile:
        lines = signalFile.readlines()

    return lines

if __name__ == "__main__":
    ret = getRejectedEntries()
    print(ret)
    ret = getEmployeesWithIDs()
    print(ret)
    ret = getEmployeesWithPhones()
    print(ret)
    ret = getEmployeesWithStates()
    print(ret)
    ret = getEmployeesWithoutIDs()
    print(ret)
    ret = getEmployeesWithoutPhones()
    print(ret)
    ret = getEmployeesWithoutStates()
    print(ret)
    ret = getCompleteEntries()
    print(ret['Watkins Chester'])
