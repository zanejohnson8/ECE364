#! /usr/local/bin/python3.4

def loadFile():

    with open("signals.txt", "r") as signalFile:
        lines = signalFile.readlines()

    return lines


def getAverageBySignal(signalName):
    pass
    lines = loadFile()
    i = 0
    avg = 0
    cor = 0
    line1 = lines[0].split()

    while (i < 9):
        if (line1[i] == str(signalName)):
            cor += 1
            col = i
        i += 1
    i = 2
    if (cor == 0):
        return "None"
    else:
        while (i < 102):
            line = lines[i].split()
            avg += float(line[col + 1])
            i += 1
        avg /= 100
        avg = round(float(avg), 2)
        return avg


def getAverageByDay(day):
    pass
    i = 0
    lines = loadFile()
    cor = 0
    avg = 0
    while (i < 102):
        col1 = lines[i].split()
        if (col1[0] == str(day)):
             cor += 1
             line_ = i
        i += 1
    i = 1
    if (cor == 0):
        return "None"
    else:
        line = lines[line_].split()
        while (i < 10):
            avg += float(line[i])
            i += 1
        avg /= 9
        avg = round(float(avg),2)
        return avg



def split(l, n):
    pass
    i = 0
    s = 0
    length = len(l)
    iter1 = length / n
    iter2 = int(length / n)
    if (iter1 >= iter2):
        iter = iter2 + 1
    v = [None] * int(iter)
    while (i < iter):
        temp_list = l[s:n]
        s = n
        n += n
        v[i] = temp_list
        i += 1
    return v

def getPalindromes():
    pass
    i = 100
    j = 100
    k = 0
    cnt = 0
    l = set()
    while (i < 1000):
        while (j < 1000):
            chk = i * j
            length = len(str(chk))
            # print("{0}".format(length))
            while (k < 3 and length == 6):
                chk2 = list(str(chk))
                #print("{0} {1}".format(chk2[k], chk2[5-k]))
                if (chk2[k] == chk2[5 - k]):
                    cnt += 1
                if (cnt == 3 and length == 6 and len(str(i)) == 3 and len(str(j)) == 3):
                    #print("{0} {1}".format(chk, cor_cnt))
                    l.add(int(chk))

                k += 1
            cnt = 0
            k = 0
            j += 1
        j = 100
        i += 1

    l = list(l)
    l.sort()
    return l

def getWords(sentence, c):
    pass
    s = sentence.split()
    length = len(s)
    i = 0
    k = 0
    fin_list = set()

    while (i < length):
        l = s[i]
        temp = list(s[i])
        wordLen = len(temp)

        if (temp[0]  == c or temp[wordLen-1] == c):
            fin_list.add(str(l))
        i += 1
    return fin_list
def getCumulativeSum():
    pass
    i = 1
    k = 1
    sum = 0
    l = []
    while (i < 101):
        while (k < i + 1):
            sum += k
            k += 1
        l.append(int(sum))
        sum = 0
        k = 1
        i += 1
    return l


def transpose(mat):
    pass
    numcol = len(mat)
    numrow = len(mat[0])
    ret = []
    temp_list = []
    i = 0
    k = 0
    while (i < numrow):
        while (k < numcol):
            temp_list.append(mat[k][i])
            k += 1
        ret.append(temp_list)
        temp_list = []
        k = 0
        i += 1
    return ret

def partition(stream):
    pass
    l = str(stream)

    temp_list = []
    ret = []
    i = 1
    length = len(l)
    cur_bit = l[0]
    temp_list.append(l[0])
    while (i < length):
        if (l[i] == cur_bit):
            temp_list.append(l[i])
        else:
            ret.append(''.join(temp_list))
            temp_list = []
            cur_bit = l[i]
            temp_list.append(l[i])
        i += 1
    ret.append(''.join(temp_list))
    return ret


def getTheSolution():
    pass

if __name__ == "__main__":

    avg = getAverageBySignal("T1")
    print("{0}".format(avg))
    avg = getAverageByDay("03/12")
    print("{0}".format(avg))
    l = getPalindromes()
    print("{0}".format(l))
    v = [11,18,15,21,19,13,14,17]
    v = split(v,3)
    print("{0}".format(v))
    s = "the power of this engine matches that of the one we had last year"
    list = getWords(s, "r")
    print(list)
    list = getCumulativeSum()
    print(list)
    mat = [[9,1], [1,3], [3,1]]
    mat = transpose(mat)
    print(mat)
    s = "0001111110111100000100"
    s = partition(s)
    print(s)