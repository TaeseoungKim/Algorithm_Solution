import sys
input = sys.stdin.readline
TestCase = int(input())

for i in range(TestCase):

    opcode = input().strip()
    strLen = int(input().strip())
    temp = input().strip()
    if temp == "[]":
        ArrStr = []
    else:
        ArrStr = temp[1:-1].split(",")
    isError = False
    isReversed = False
    leftPopped = 0
    rightPopped = 0

    for op in opcode:
        if op == "R":
            isReversed = not isReversed
        elif op == "D":
            if leftPopped+rightPopped >= len(ArrStr):
                isError = True
            else:
                if not isReversed:
                    leftPopped += 1
                else:
                    rightPopped += 1

    if isError:
        print("error")
    else:
        if len(ArrStr) == 0:
            print("[]")
        elif isReversed:
            ArrStr = list(reversed(ArrStr))
            if leftPopped == 0:
                print(
                    str(ArrStr[rightPopped:]).replace(" ", "").replace("'", ""))
            else:
                print(
                    str(ArrStr[rightPopped:-(leftPopped)]).replace(" ", "").replace("'", ""))

        else:
            if rightPopped == 0:
                print(
                    str(ArrStr[leftPopped:]).replace(" ", "").replace("'", ""))
            else:
                print(
                    str(ArrStr[leftPopped:-(rightPopped)]).replace(" ", "").replace("'", ""))
