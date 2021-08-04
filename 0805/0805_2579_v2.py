stair_cnt = int(input())
stair_point = [ 0 for _ in range(301) ] # 처음에는 for문을 stair_cnt만큼만 돌려줬는데 index error가 났다. 
sum = [ 0 for _ in range(301) ]         # 이유가 궁금하다

for _ in range(stair_cnt):
    stair_point[_] = int(input())

sum[0] = stair_point[0]
sum[1] = stair_point[0] + stair_point[1]
sum[2] = max(stair_point[0]+stair_point[2],stair_point[1]+stair_point[2])

if 1 <= stair_cnt <= 3:
    print(sum[stair_cnt-1])
    exit()

for i in range(3,stair_cnt,1):
    sum[i] = max( sum[i-3] + stair_point[i-1] + stair_point[i] , sum[i-2] + stair_point[i] )

print(sum[stair_cnt-1])