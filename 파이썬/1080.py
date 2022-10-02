import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [ list(map(int, input().strip())) for i in range(N) ]
B = [ list(map(int, input().strip())) for i in range(N) ]
cnt = 0
flag = 0
def transition(i,j):
    global cnt
    cnt += 1
    for a in range(i,i+3,1):
        for b in range(j,j+3,1):
            if A[a][b]==1:
                A[a][b]=0
            else:
                A[a][b]=1

for a in range(N-2):
        for b in range(M-2):
            if A[a][b] != B[a][b]:
                transition(a,b)

for i in range(N): # 변환 후 일치하는지 확인
    for j in range(M):
        if A[i][j] != B[i][j]:
            flag = 1
            break

if flag == 1:							# 변환이 불가능 하면 -1 반환
    print(-1)
else:
    print(cnt)