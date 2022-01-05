import sys

_ , C = map(int,input().split())
N = sorted(list( int(sys.stdin.readline()) for _ in range(_)))

print(N)