import sys
input = sys.stdin.readline

zero_area = 0
one_area = 0
current_area = 0
S = input()

current_area = S[0]
if current_area=='0':
    zero_area += 1
else:
    one_area += 1

for i in range(1,len(S)-1):  
    if S[i] != current_area:
        if current_area== '0':
            one_area += 1
        else:
            zero_area += 1
        current_area = S[i]
    
print(min(int(zero_area),int(one_area)))