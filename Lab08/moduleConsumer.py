import moduleTasks

def loadSignals(signalNames, signalFolder, maxNonfloatCount):
    ret = dict()
    for name in signalNames:
        try:
            v,c = moduleTasks.loadSignal(name, signalFolder)
        except:
            ret.update({name:None})
        else:
            if (c <= maxNonfloatCount):
                ret.update({name:v})
            elif (c > maxNonfloatCount):
                ret.update({name:[]})
    return ret

def saveSignals(signalsDictionary, valueRange, maxCount, targetFolder):

    final = str()
    for name in signalsDictionary.keys():
        if signalsDictionary[name] != None and signalsDictionary[name] != []:
            chk = moduleTasks.isSignalAcceptable(signalsDictionary[name], valueRange, maxCount)
            if (chk == True):
                fp = open('./' + targetFolder + '/' + name + '.txt', "w")
                length = len(signalsDictionary[name])
                i = 0
                for num in signalsDictionary[name]:
                    if (i < length - 1):
                        s = "\n"
                    else:
                        s = ""
                    fp.write("{0:.3f}".format(num))
                    fp.write(s)
                    i += 1
                fp.close()


if __name__ == "__main__":
    ret = loadSignals(["AFW-481", "REY-386", "WAE-386", "HPQ-298"], "Signals", 7)
    ret0 = saveSignals(ret, (-12.0, 11.7), 20, "Test")