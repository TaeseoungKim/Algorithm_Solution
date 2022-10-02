



def solution(p, c):
    participant = dict()
    completion = dict()
    for name in p:
        if participant.get(name)==None:
            participant[name]=1
        else: participant[name]+=1
    for name in c:
        participant[name]-=1
    for name in p:
        if participant[name]==1:
            return name