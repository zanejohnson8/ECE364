def loadFile(s):

    with open(s, "r") as signalFile:
        lines = signalFile.readlines()

    return lines

if __name__ == "__main__":
	lines = loadFile("signals.txt")
    	
