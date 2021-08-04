T = int(input())

for a in range(T):
    n = int(input())
    fibonacci = [1] 
    for b in range(1,n+1):
        fibonacci.append( fibonacci[b-1] + b-1 )    
    print(fibonacci[n])