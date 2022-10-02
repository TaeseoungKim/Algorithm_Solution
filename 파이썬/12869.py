# https://www.acmicpc.net/source/39048615
# dp문제는 되도록이면 메모리를 많이 쓰더라도, 속도면에서 dp를 쓰는 것이 현명하다.
when = [[1,3,9],[1,9,3],[3,1,9],[3,9,1],[9,3,1],[9,1,3]]
n=int(input())
MAX_HP = 61
tmp_hp = list(map(int,input().split()))
visited = [[[MAX_HP]*MAX_HP for _ in range(MAX_HP)] for _ in range(MAX_HP)]


def dp(position):
    for i in range(3):
        if position[i]<0:
            position[i]=0
    if sum(position)==0:
        return 0

    least=visited[position[0]][position[1]][position[2]]
    
    if least != MAX_HP:
        return least

    for attack in when:
        least = min(least, dp([position[0]-attack[0],position[1]-attack[1],position[2]-attack[2]]))

    least+=1
    visited[position[0]][position[1]][position[2]]=least
    return least

p = [0]*3
for i in range(n):
    p[i] = tmp_hp[i]
print(dp(p))