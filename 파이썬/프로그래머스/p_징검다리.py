



def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    print(rocks)
    left=0
    right=distance
    mid=0
    cnt=0
    cur_rock=0
    while left<=right:
        mid=(left+right)//2
        if rocks[cur_rock]-left <= distance:
            cnt+=1
            cur_rock+=1
        else:
            right=mid-1

            
            


    return answer


distance=25	
rocks=[2, 14, 11, 21, 17]	
n=2
solution(distance, rocks, n)