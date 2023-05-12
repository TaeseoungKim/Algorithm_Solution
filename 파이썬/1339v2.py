import sys
input = sys.stdin.readline


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
