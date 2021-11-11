import sys
input = sys.stdin.readline
 
N = int(input())
M = int(input())

Nroot = [i for i in range(N+1)]
Mlist = []

for _ in range(M):
    Mlist.append(list(map(int, input().split())))
 
Mlist.sort(key=lambda x: x[2]) # 크루스칼 알고리즘을 적용하기 위해 가중치 기준으로 정렬
 
 
def find(x):
    if x != Nroot[x]:
        Nroot[x] = find(Nroot[x])
    return Nroot[x]
 
 
answer = 0
for s, e, w in Mlist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Nroot[sRoot] = eRoot
        else:
            Nroot[eRoot] = sRoot
        answer += w
 
print(answer)