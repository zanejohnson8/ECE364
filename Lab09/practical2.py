import re

def getNumericData(sentence):
    l = re.findall(r"\w+|\S+", sentence)
    ret = []
    for num in l:
        expr = r"(?P<integer>^[+-][0-9]+[^.,])"
        match = re.match(expr, num)
        if (match):
            ret.append(match.group('integer'))
        expr = r"(?P<float>^[+-]?[\d]+.[\d]+[^eE]$)"
        match = re.match(expr, num)
        if (match):
            ret.append(match.group('float'))
    return ret

def parseSimple(fileName):
    lines = loadFile(fileName)
    ret = dict()

    for word in lines:
        expr = r"\"(?P<key>[a-zA-Z]+)\"\s?:\s?\"(?P<val>[A-Za-z\s.,0-9#-]+)\""
        match = re.search(expr, word)
        if (match):
            ret.update({match.group('key'):match.group('val')})
    return ret
def parseLine(fileName):
    lines = loadFile(fileName)
    ret = dict()
    exp1 = r"(\"[A-Za-z\s.,0-9#-]+\")"
    l = re.findall(exp1, lines[0])
    i = 0
    length = len(l)
    while i < length:
        expr = r"\"(?P<val>[A-Za-z\s.,0-9#-]+)\""
        match = re.search(expr, l[i])
        match1 = re.search(expr, l[i+1])
        if (match and match1):
            ret.update({match.group('val'):match1.group('val')})
        i += 2
    return ret


def parseComplex(fileName):
    lines = loadFile(fileName)
    ret = dict()
    for word in lines:
        expr = r"\"(?P<key>[a-zA-Z]+)\"\s?:\s?\"(?P<val>[A-Za-z\s.,0-9#-]+)\""
        match = re.search(expr, word)
        if (match):
            ret.update({match.group('key'):match.group('val')})
        expr = r"\"(?P<key>[a-zA-Z]+)\"\s?:\s?(?P<val>true|false|[0-9.+-]+)"
        match = re.search(expr, word)
        if (match):
            ret.update({match.group('key'):match.group('val')})
    return ret


def parseComposite(fileName):
    lines = loadFile(fileName)
    ret = dict()
    for word in lines:
        temp = []
        expr = r"\"(?P<key>[a-zA-Z]+)\"\s?:\s?\"(?P<val>[A-Za-z\s.,0-9#-:]+)\""
        match = re.search(expr, word)
        if (match):
            ret.update({match.group('key'):match.group('val')})
        expr = r"\"(?P<key>[a-zA-Z]+)\"\s?:\s?(?P<val>true|false|[0-9.+-]+)"
        match = re.search(expr, word)
        if (match):
            ret.update({match.group('key'):match.group('val')})
        expr = r"\"(?P<key>[a-zA-Z]+)\"\s?:\s?\[(?P<val>\s?[a-zA-Z0-9\",\s+-]+)\s?\],?"
        match = re.search(expr, word)

        if (match):
            exp1 = r"\w+"
            s = str(match.group('val'))
            m = re.findall(exp1, s)
            ret.update({match.group('key'):m})
    return ret


def loadFile(s):

    with open(s, "r") as signalFile:
        lines = signalFile.readlines()
    return lines

if __name__ == "__main__":
    s = "With the electron's charge being -1.6022e-19, some choices you have are -110, -32.0, +55. Assume that pi equals 3.1415, 'e' equals 2.7 and Na is +6.0221E+023"
    ret = getNumericData(s)
    print(ret)
    ret = parseSimple("simple.json")
    ret = parseLine("simple2.json")
    ret = parseComplex('complex.json')
    ret = parseComposite('composite.json')
    print(ret)