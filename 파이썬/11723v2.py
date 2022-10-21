import sys
input = sys.stdin.readline
M = int(input())
Ans = set()
for i in range(M):
    op = input().split()
    if len(op) == 2:
        x = int(op[1])
    op = op[0]

    if op == "add":
        Ans.add(x)
    elif op == "remove":
        if x in Ans:
            Ans.remove(x)
    elif op == "check":
        if x in Ans:
            print(1)
        else:
            print(0)
    elif op == "toggle":
        if x in Ans:
            Ans.remove(x)
        else:
            Ans.add(x)
    elif op == "all":
        Ans = set(range(1, 21))
    elif op == "empty":
        Ans = set()
