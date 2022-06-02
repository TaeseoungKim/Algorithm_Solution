n = int(input())
board = [1]*1000000
# 100만번까지의 소수를 다 구해놓음
for i in range(1000000):
    if i == 0 or i == 1:
        board[i]=0
        continue
    if board[i]==1:
        for d in range(i+i,1000000,i):
            if board[d]==1:
                board[d]=0

def isPalindrome(word):
    if word == word[::-1]:
        return True
    return False

for i in range(n,1000000):
    if isPalindrome(str(i)) and board[i]==1:
        print(i)
        break

if n==1000000:
    print(1003001)