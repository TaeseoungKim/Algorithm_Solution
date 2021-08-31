name = input()
name = list(name)

result = []
name.sort(reverse=True) # 내림차순으로 정렬
is_exist_middle = 0 # 

i = 0
while i != len(name) : # 2개씩 증가 ddccbbaa 
    if(i+1 == len(name)): #
        if(is_exist_middle == 1): #이미 존재하면 불가능한 것
            print("I'm Sorry Hansoo")
            exit(0)
        
        middle = len(result)//2 
        result.insert(middle,name[i]) 
        is_exist_middle = 1 
        i -= 1 
        break 
    
    if(name[i] == name[i+1]) : #같을 경우
        result.insert(0,name[i]) 
        result.append(name[i+1]) 
    else:                       #다를 경우
        if(is_exist_middle == 1): 
            print("I'm Sorry Hansoo") 
            exit(0) 
        
        middle = len(result)//2
        result.insert(middle,name[i])
        is_exist_middle = 1
        i -= 1
    i += 2


result = "".join(result) #리스트를 문자열로
print(result)