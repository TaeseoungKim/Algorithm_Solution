# 7
# 1 2 1 3 1 2 1
# 4
# 1 3
# 2 5
# 3 3
# 5 7

import sys
input = sys.stdin.readline

N = int(input())
inputArr = list(input().split(" "))
inputStr = ""

for i in range(len(inputArr)):
    inputStr += inputArr[i]

print("답")

T = int(input())
for i in range(T):
    left, right = map(int, input().split())
    print("테스트:", inputStr[left-1:right], reversed(inputStr[left-1:right]))
    if inputStr[left-1:right] == reversed(inputStr[left-1:right]):
        print(1)
    else:
        print(0)
