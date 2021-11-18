import sys
input = sys.stdin.readline

input_list = sorted(list(map(int,input().strip())),reverse=True)

for _ in input_list:
    print(_,sep='',end='')
