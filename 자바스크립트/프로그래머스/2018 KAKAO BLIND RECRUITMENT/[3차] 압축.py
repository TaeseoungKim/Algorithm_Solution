
from string import ascii_uppercase


def solution(msg):
    msgLen = len(msg)
    dic = dict()
    result = []

    for i in range(1, len(ascii_uppercase)+1):
        dic[ascii_uppercase[i-1]] = i

    curIdx = 0
    while True:
        w = ""
        startIdx = curIdx
        for i in range(curIdx, msgLen):
            if msg[curIdx:i+1] in dic:
                w = msg[curIdx:i+1]
                startIdx = i
            elif msg[curIdx:i+1] not in dic:
                dic[msg[curIdx:i+1]] = len(dic) + 1
                curIdx = i
                break

        result.append(dic[w])
        if startIdx == msgLen-1:
            break
    return result
