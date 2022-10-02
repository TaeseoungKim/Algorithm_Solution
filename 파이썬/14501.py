import sys
input = sys.stdin.readline
N = int(input())
T, P = [],[]
board = [0]*(N+1)
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
maxV=0
for i in range(N-1,-1,-1):
    if N < i+T[i]:
        board[i]=board[i+1]
    else:
        board[i]=max(board[i+1],P[i]+board[i+T[i]])
print(board[0])