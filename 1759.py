#4 6
# a t c i s w

def dfs(cur,idx,cnt):

    if cnt==l:
        if visited.get(cur)==None:
            aeiou=0
            aeiou_else=0
            for c in cur:
                if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
                    aeiou+=1
                else: aeiou_else+=1
                if aeiou>=1 and aeiou_else>=2:
                    result.append(cur)
                    break
            visited[cur]=1
        return
    for i in range(idx,k):
        next=cur+str(pw[i])
        dfs(next,i+1,cnt+1)
    return

l,k = map(int, input().split())
pw = list(input().split())
pw.sort()
result=[]
visited = dict()
dfs("",0,0)
for s in result:
    print(s)
    