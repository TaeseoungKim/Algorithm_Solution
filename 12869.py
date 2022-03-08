# https://www.acmicpc.net/source/39048615
n=int(input())
tmp_hp = list(map(int,input().split()))
scv_hp = [0]*3
for i in range(n):
    scv_hp[i]=tmp_hp[i]

cnt=0
hp_dict = dict()

min_V = 999
def dfs(hp,cnt):
    global min_V
    t1,t2,t3 = hp
    if t1<=0 and t2<=0 and t3<=0:
        if min_V>cnt:
            min_V=cnt
        return

    for next_t1,next_t2,next_t3 in [(t1-9,t2-3,t3-1),(t1-9,t2-1,t3-3),(t1-3,t2-1,t3-9),(t1-3,t2-9,t3-1),(t1-1,t2-3,t3-9),(t1-1,t2-9,t3-3)]:
        if hp_dict.get((next_t1,next_t2,next_t3,cnt+1))==None:
            hp_dict[(next_t1,next_t2,next_t3,cnt+1)]=1
            dfs((next_t1,next_t2,next_t3),cnt+1)
dfs(scv_hp,cnt)
print(min_V)