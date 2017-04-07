import re

def isNameValid(signalName):
    expr = r"^[A-Z]{3}-[0-9]{3}$"
    match = re.search(expr, signalName)
    if (match):
        return True
    else:
        return False


def loadSignal(signalName, signalFolder):
    chk = isNameValid(signalName)
    v = []
    c = 0
    if (chk == False):
        raise ValueError("{0} is invalid.".format(signalName))
        return 0,0
    else:
        try:
            s = "./" + signalFolder + "/" + signalName + ".txt"
            lines = loadFile(s)
        except FileNotFoundError:
            raise OSError("{0} is invalid.".format(signalName))
            return 0,0
        else:
            for line in lines:
                f = line[:-1]
                try:
                    temp = float(f)
                except ValueError:
                    c += 1
                else:
                    v.append(temp)

            return v,c


def isSignalAcceptable(signal, valueRange, maxCount):
    cnt = 0
    if len(signal) == 0:
        raise ValueError("Signal contains no data.")
        return
    else:
        for el in signal:
            if (el > valueRange[1] or el < valueRange[0]):
                cnt += 1
        if (cnt > maxCount):
            return False
        else:
            return True



def loadFile(s):

    with open(s, "r") as signalFile:
        lines = signalFile.readlines()
    return lines


if __name__ == "__main__":
    ret = isNameValid("AFE-996")
    print(ret)
    ret = isNameValid("WAZE-386")
    print(ret)
    ret = isNameValid("XYZ-2020")
    print(ret)
    v,c = loadSignal("REY-386", "Signals")
    print(v,c)
    print(isSignalAcceptable(v, (-12.0, 11.7), 5))
    print(isSignalAcceptable(v, (-12.0, 11.7), 20))