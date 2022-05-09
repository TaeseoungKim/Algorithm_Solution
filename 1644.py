n = int(input())
a = [False,False] + [True]*(n-1)
primes=[]
for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
board = [0]*len(primes)
answ=0
left, right= 0,len(primes)-1
dp = [[0]*(n+1) for _ in range(n+1)]
#아 뒤부터 해야되겟구나

for i in range(len(primes)):
    board[i]=primes[i]
    for d in range(i+1,len(primes)):
        if dp[i][d]!=0:
            continue
        else:
            if primes[d]==n:
                answ+=1
                break
            board[d]=board[d-1]+primes[d]
            dp[i][d]=board[d]
            if board[d]==n:
                answ+=1
                break
            elif board[d]>n:
                break
    board = [0]*len(primes)
print(answ)