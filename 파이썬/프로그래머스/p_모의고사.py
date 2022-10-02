# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5,
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5

def solution(answers):
    person1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    p1,p2,p3 = 0,0,0
    p1_max,p2_max,p3_max = len(person1),len(person2),len(person3)
    result = [0]*3
    for i in range(len(answers)):
        if p1==p1_max:p1=0
        if p2==p2_max:p2=0
        if p3==p3_max:p3=0

        if answers[i]==person1[p1]:
            result[0]+=1
        if answers[i]==person2[p2]:
            result[1]+=1
        if answers[i]==person3[p3]:
            result[2]+=1

        p1+=1
        p2+=1
        p3+=1
    max_v = max(result)
    res = []
    for i in range(3):
        if result[i]==max_v:
            res.append(i+1)
    return res

answers	= [1,3,2,4,2]
print(solution(answers))
