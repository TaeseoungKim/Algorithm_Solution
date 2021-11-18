import sys
input = sys.stdin.readline

N = int(input())
N_list = [ int(input()) for _ in range(N) ]

for _ in sorted(N_list):
    print(_)
