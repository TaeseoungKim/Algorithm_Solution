import sys
input = sys.stdin.readline
n, k = map(int, input().split())
board = list(map(int, input().strip()))
answ=[]
print(board)
print("index:",board.index(7))

idx=-1
for i in range(1,n-k+1):
    print(idx+1,k+i)
    maxVal=max(board[idx+1:k+i])
    idx = board.index(maxVal,idx+1,k+i)+1
    answ.append(maxVal)
    print("냠냠",idx,maxVal)
print(*answ,sep="")