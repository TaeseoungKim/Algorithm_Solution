import sys
sys.setrecursionlimit(1000000)

# n-2가 방문되어있으면 1불가능 2만가능
# n-2가 방문되어있지않으면 1도 가능하고 2도 가능하다

stair_cnt = int(input())
stair_point = [0]
for _ in range(stair_cnt):
    stair_point.append( int(input()) )

result_list = [[0] for _ in range(stair_cnt+1)]
visit_list = [ 0 for _ in range(stair_cnt+1) ]

def stair(n , p_visit , p_sum):
    print("저는 %d 입니다 "%n)
    if stair_cnt < n :
        return
    
    tmp_visit = p_visit[:]
    tmp_sum = p_sum + stair_point[n]
    tmp_visit[n] = 1 if n != 0 else 0
    
    if stair_cnt == n and tmp_visit[n-2] == 1 and tmp_visit[n-1] == 1:
        return
    elif max(result_list[n]) >= tmp_sum and n != 0 :
        return
    else :
        result_list[n].append(tmp_sum)   

#가능한지 불가능한지를 두자

    if tmp_visit[n-2] == 1 and tmp_visit[n-1] == 1 :
        stair(n+2,tmp_visit,tmp_sum)
    else:
        stair(n+1,tmp_visit,tmp_sum)
        stair(n+2,tmp_visit,tmp_sum)


stair(0,visit_list,0)
max_result = max(map(max, result_list))
print(result_list)
print(max_result)
