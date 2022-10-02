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
left,right=0,0

while right < len(primes):
    sumV=sum(primes[left:right+1])
    if sumV==n:
        answ+=1
        right+=1
    elif sumV>n:
        left+=1
    else:
        right+=1
print(answ)