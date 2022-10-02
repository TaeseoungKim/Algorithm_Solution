import sys
input = sys.stdin.readline

beforeStr = input().strip()
beforeStr_Len = len(beforeStr)
doubleColonPos = beforeStr.find('::')
conlonCnt = beforeStr.count(':')

temp=""
if doubleColonPos==0: 
    for _ in range(7-conlonCnt+2):
        temp+="0000:"
elif doubleColonPos==beforeStr_Len-2: # ::이 맨 뒤에 있을 때
    for _ in range(7-conlonCnt+2):
        temp+=":0000"
elif doubleColonPos!=-1: # ::이 중간에 있을 때
    temp=":"
    for _ in range(7-conlonCnt+1):
        temp+="0000:"
    
beforeStr = beforeStr.replace("::",temp)
beforeStr_Len = len(beforeStr)
afterStr = []
numberCnt = 0
for i,c in enumerate(beforeStr):
    afterStr.append(c)
    numberCnt+=1
    if c==':':
        if numberCnt<6:
            for _ in range(5-numberCnt):
                afterStr.insert(-numberCnt,'0')
        numberCnt=0
    elif i==beforeStr_Len-1:
        if numberCnt<5:
            for _ in range(4-numberCnt):
                afterStr.insert(-numberCnt,'0')
print("".join(afterStr))    
