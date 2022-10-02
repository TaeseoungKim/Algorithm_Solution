import sys
input = sys.stdin.readline  
left = right = 0
result = ""
check = 0

def startWithleft(p):
    global left, right, result
    if len(p)==0:
        return     
    for i,c in enumerate(p):
        if '(' == c:
            left += 1
        elif ')' == c:
            right += 1
        if right == left:
            result += p[:i+1]
            if p[i+1] != 'e':
                solution(p[i+1:])
            return   
        
        
def startWithright(p):
    global left, right, result
    tmp_p = ""
    for i,c in enumerate(p):
            if '(' == c:
                left += 1
                tmp_p += ')'
            elif ')' == c:
                right += 1
                tmp_p += '('
            if right == left:
                result += tmp_p
                if p[i+1] != 'e':
                    solution(p[i+1:])
                return

def solution(p):
    global left, right, result
    if len(p)==0:
        return ""
    if p[0] == '(':
        startWithleft(p+"e")
    elif p[0] == ')':
        startWithright(p+"e")
    return result

print(solution(")()()()("))