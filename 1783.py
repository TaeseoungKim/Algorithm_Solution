low, column = map(int,input().split())

if (low > 2000000000) or (column > 2000000000):
    exit(0)

#문제를 보며 좌우로는 오른쪽으로 밖에 움직이지 못한다는 것을 인지
#
#low가 1일 때는 움직이지 못하므로 1 출력
#low가 2일 때는 상하 1씩 이므로 오른쪽으로 2칸씩 이동하는 방법으로 최대 3번 이동 가능
#low가 3이상일때는 이동횟수가 4미만일때와 4이상일때를 구별한다

#이동횟수가 4이상일 때는 적어도 모든 방법을 1번씩 사용해야 하므로 column이 7이상일 때 이다.
#한번씩 사용했으므로 5를 더한 상태에서 1칸씩만 움직이면되므로 나머지 column을 더해준다
# 5
#4번 미만일 때는 최대로 이동해야 하므로 먼저 오른쪽으로 1칸씩 2번움직이고 오른쪽으로 2칸 1번을 하는 방법이 최대이다.
#아니라면 그냥 column수가 되겟지
#그러므로 min(column,4)

# 런타임에러 이유 low, column = map(int,input().split())

if low == 1 : 
    print(1)
elif low == 2 : # 4, (M + 1) / 2
    if (column+1) // 2 < 4 : # 
        max = (column+1) // 2
        print(max)
    else :
        print(4)
elif low >= 3 :
    if column >= 7 :
        max = column - 2
        print(max)
    elif 4 > column :
        print(column)
    else :
        print(4)

exit(0)


