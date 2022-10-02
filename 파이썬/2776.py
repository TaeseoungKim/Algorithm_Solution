import sys
input = sys.stdin.readline

T = int(input())

def Search():

    N = int(input())
    N = sorted(list( map(int, input().split())))
    M = int(input())
    M = list( map(int, input().split() ) )
    
    for value in(M):


        start , end = 0 , N.__len__()-1    
        while start <= end :
            is_found = False
            mid = (start+end)//2
            if value > N[mid]:
                start = mid+1
            elif value < N[mid]:
                end = mid-1
            elif value == N[mid]:
                is_found = True
                break
        print(1 if is_found == True else 0)


for _ in range(T):
    Search()
