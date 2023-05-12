import sys
from itertools import permutations
from copy import deepcopy
input = sys.stdin.readline

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def calResult(tempAlphaDict):
    tempBoard = []
    for word in board:
        tempWord = ""
        for c in word:
            tempWord += tempAlphaDict[c]
        tempBoard.append(int(tempWord))

    sumN = 0
    for num in tempBoard:
        sumN += num
    return sumN


TestCase = int(input())
board = []
alphaDict = dict()

for i in range(TestCase):
    word = input().strip()
    board.append(word)
    for c in word:
        if c in alphaDict:
            continue
        else:
            alphaDict[c] = 0

alphaList = list(alphaDict.keys())
alphaCnt = len(alphaList)
result = []
for per in permutations(numbers[-1:-(alphaCnt+1):-1], alphaCnt):
    tempAlphaDict = deepcopy(alphaDict)
    for num in range(len(per)):
        tempAlphaDict[alphaList[num]] = per[num]
    result.append(calResult(tempAlphaDict))
print(max(result))
