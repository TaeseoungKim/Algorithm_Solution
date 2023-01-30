import sys
input = sys.stdin.readline

inputStr = input().strip()
print(inputStr)

strDict = dict()
for c in inputStr:
    if c in strDict:
        strDict[c] += 1
    else:
        strDict[c] = 1

board = ''
newBoard = ''
for c in inputStr.keys():
    if board == '':
        board += c
        continue
    newBoard = board + c