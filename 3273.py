import sys
input = sys.stdin.readline
n = int(input())
board = list(map(int, input().split()))
x = int(input())
board.sort()

left=0
right=n-1
answ=0
while left<right:
    sumV = board[left]+board[right]
    if x==sumV:
        left+=1
        right-=1
        answ+=1
    # 값을 높여야할 때 : left+=1
    elif x>board[left]+board[right]:
        left+=1
    # 값을 낮춰야할 때 : right-=1
    elif x<board[left]+board[right]:
        right-=1
print(answ)