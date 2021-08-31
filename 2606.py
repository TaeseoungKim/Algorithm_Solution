import sys
sys.setrecursionlimit(1000000)

def dfs(v):
    global virus_cnt    
    visit[v] = 1

    for i in range(n):
        if visit[i] == 1 or v == i :
            continue
        elif network[v][i] == 1 and visit[i] == 0 :
            virus_cnt += 1
            dfs(i)


n = int(input())
k = int(input())

network = [ [0] * n for _ in range(n) ]
visit = [ 0 for _ in range(n) ]
virus_cnt = 0

for _ in range(k):
    a , b = map(int , input().split())
    # 문제에서 1번 컴퓨터부터 시작하기 때문에, -1을 해주어 인덱스를 맞춰준다
    network[a-1][b-1] = 1
    network[b-1][a-1] = 1

dfs(0)
print(virus_cnt)
