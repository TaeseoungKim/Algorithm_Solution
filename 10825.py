# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90
import sys
input = sys.stdin.readline
grade = []

N = int(input())
for _ in range(N):
    name, kor, eng, math = input().split()
    grade.append((name, int(kor), int(eng), int(math)))
    
    
grade.sort(key=lambda x : (-x[1],x[2],-x[3],x[0]))
for _ in range(N):
    print(grade[_][0])