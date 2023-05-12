import sys
input = sys.stdin.readline
TestCase = int(input())
board = []
alphaDict = dict()


for i in range(TestCase):
    word = input().strip()
    board.append(word)
    wordLen = len(word)

    for index, c in enumerate(word):
        if c not in alphaDict:
            alphaDict[c] = 0
        alphaDict[c] += 10**(wordLen-(index+1))

alphaTupleList = []
for key in alphaDict.keys():
    alphaTupleList.append((key, alphaDict[key]))

alphaTupleList.sort(key=lambda x: -x[1])
keyLen = len(alphaDict.keys())

curIdx = 0
sumVal = 0
for i in range(9, 9-keyLen, -1):
    _, Value = alphaTupleList[curIdx]
    sumVal += Value*i
    curIdx += 1


print(sumVal)
