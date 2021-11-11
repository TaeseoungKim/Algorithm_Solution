def hanoi (count,start,end,assist) :
    if count == 1 :
        print(start,end)
        return
    hanoi(count-1,start,assist,end)
    print(start,end)
    hanoi(count-1,assist,end,start)

N = int(input())

print(2**N - 1) # 2^N -1
if N <= 20:
    hanoi(N,1,3,2)