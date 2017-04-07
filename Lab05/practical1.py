
def getSummary():
    ret = dict()
    lines = loadFile("./signals.txt")
    length = len(lines)
    firstline = lines[0].split()
    i = 1
    while (i < len(firstline)):
        ret.update({firstline[i]:(0,0,0)})
        i += 1
    i = 2
    while (i < len(firstline)):
        x = 3
        avg = float(0)
        min = float(9999999)
        max = float(0)
        while (x < length):
            templine = lines[x].split()
            avg += float(templine[i])
            if (float(templine[i]) <= float(min)):
                min = templine[i]
            if (float(templine[i]) >= float(max)):
                max = templine[i]
            x += 1
        avg /= (x + .677)
        avg1 = round(avg, 3)
        t = (min, avg1, max)
        ret[firstline[i]] = t
        i += 1
    return ret


def saveContinuousData(start, end, targetFileName):
    pass


def getSampledSignal(signalName):
    pass


def identifyCheapest(componentSet):
    ret = dict()
    CDW = loadFile("./Sources/CDW.txt")
    eBay = loadFile("./Sources/eBay.txt")
    Gov = loadFile("./Sources/GovConnection.txt")
    Target = loadFile("./Sources/Target.txt")
    min = 9999999999
    name = str()
    for comp in componentSet:
        len1 = len(CDW)
        i = 3
        while (i < len1):
            tempLine = CDW[i].split()
            s = str(str(tempLine[0]) + ' ' + str(tempLine[1]))
            num = list(tempLine[3])

            if (s == comp):
                if (float(''.join(num[1:])) <= min):
                    min = float(''.join(num[1:]))
                    name = 'CDW'
            i += 1

        len2 = len(eBay)
        i = 3
        while (i < len2):
            tempLine = eBay[i].split()
            s = str(str(tempLine[0]) + ' ' + str(tempLine[1]))
            num = list(tempLine[3])
            if (s == comp):
                if (float(''.join(num[1:])) <= min):
                    min = float(''.join(num[1:]))
                    name = 'eBay'
            i += 1

        len3 = len(Gov)
        i = 3
        while (i < len3):
            tempLine = Gov[i].split()
            s = str(str(tempLine[0]) + ' ' + str(tempLine[1]))
            num = list(tempLine[3])
            if (s == comp):
                if (float(''.join(num[1:])) <= min):
                    min = float(''.join(num[1:]))
                    name = 'GovConnection'
            i += 1

        len4 = len(Target)
        i = 3
        while (i < len4):
            tempLine = Target[i].split()
            s = str(str(tempLine[0]) + ' ' + str(tempLine[1]))
            num = list(tempLine[3])

            if (s == comp):
                if (float(''.join(num[1:])) <= min):
                    min = float(''.join(num[1:]))
                    name = 'Target'
            i += 1

        ret.update({str(comp):(float(min), str(name))})
        min = 9999999999
        name = str()
    return ret


def getComponentsToAdd():
        ret = dict()
        CDW = loadFile("./Sources/CDW.txt")
        eBay = loadFile("./Sources/eBay.txt")
        Gov = loadFile("./Sources/GovConnection.txt")
        Target = loadFile("./Sources/Target.txt")
        st = set()
        len1 = len(CDW)
        i = 3
        while (i < len1):
            tempLine = CDW[i].split()
            s = str(str(tempLine[0]) + ' ' + str(tempLine[1]))
            num = list(tempLine[3])

            st.add(s)
            i += 1

        len2 = len(eBay)
        i = 3
        while (i < len2):
            tempLine = eBay[i].split()
            s = str(str(tempLine[0]) + ' ' + str(tempLine[1]))
            num = list(tempLine[3])
            st.add(s)
            i += 1

        len3 = len(Gov)
        i = 3
        while (i < len3):
            tempLine = Gov[i].split()
            s = str(str(tempLine[0]) + ' ' + str(tempLine[1]))
            num = list(tempLine[3])
            st.add(s)
            i += 1

        len4 = len(Target)
        i = 3
        while (i < len4):
            tempLine = Target[i].split()
            s = str(str(tempLine[0]) + ' ' + str(tempLine[1]))
            num = list(tempLine[3])
            st.add(s)
            i += 1
        flag = 0
        s1 = set()
        s2 = set()
        s3 = set()
        s4 = set()
        for elem in st:
            len1 = len(CDW)
            i = 3
            while (i < len1 and flag == 0):
                tempLine = CDW[i].split()
                s = str(str(tempLine[0]) + ' ' + str(tempLine[1]))
                num = list(tempLine[3])
                if (s == elem):
                    flag = 1
                i += 1
            if (flag == 0):
                s1.add(s)
            flag = 0

            len2 = len(eBay)
            i = 3
            while (i < len2 and flag == 0):
                tempLine = eBay[i].split()
                s = str(str(tempLine[0]) + ' ' + str(tempLine[1]))
                num = list(tempLine[3])
                if (s == elem):
                    flag = 1
                i += 1
            if (flag == 0):
                s2.add(s)
            flag = 0

            len3 = len(Gov)
            i = 3
            while (i < len3 and flag == 0):
                tempLine = Gov[i].split()
                s = str(str(tempLine[0]) + ' ' + str(tempLine[1]))
                num = list(tempLine[3])
                if (s == elem):
                    flag = 1
                i += 1
            if (flag == 0):
                s3.add(s)
            flag = 0

            len4 = len(Target)
            i = 3
            while (i < len4 and flag == 0):
                tempLine = Target[i].split()
                s = str(str(tempLine[0]) + ' ' + str(tempLine[1]))
                num = list(tempLine[3])
                if (s == elem):
                    flag = 1
                i += 1
            if (flag == 0):
                s4.add(s)
            flag = 0
        ret = {"CDW": s1, "eBay": s2, "GovConnection": s3, "Target": s4}
        return ret



def loadFile(s):

    with open(s, "r") as signalFile:
        lines = signalFile.readlines()

    return lines


if __name__ == "__main__":
    components = {'Intel i7-4700HQ', 'Intel i7-6970HQ'}
    ret = identifyCheapest(components)
    print(ret)
    ret = getComponentsToAdd()
    print(ret)
    ret = getSummary()
    print(ret)
