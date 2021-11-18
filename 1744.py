import sys
input = sys.stdin.readline

n = int(input())
negative = 0
positive = 0
zero = 0
num_list = []
result = 0

for _ in range(n):
    tmp = int(input())
    num_list.append(tmp)    
    
    if tmp < 0 :
        negative+=1
    elif tmp > 0 :
        positive+=1
    elif tmp == 0:
        zero+=1

num_list.sort()

if negative%2 == 0:
    for _ in range(0,negative,2):
        if num_list[_+1] != 0:
        result += num_list[_]*num_list[_+1]
        