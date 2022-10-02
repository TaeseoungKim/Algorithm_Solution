import sys
input = sys.stdin.readline

k = int(input())
sum_stack = []
for _ in range(k):
    tmp = int(input())
    if tmp == 0:
        sum_stack.pop()
    else: sum_stack.append(tmp)
print(sum(sum_stack))