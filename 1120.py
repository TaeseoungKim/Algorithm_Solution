import sys
input = sys.stdin.readline

str1, str2 = input().split()
str1_len = len(str1)
str2_len = len(str2)

if str1_len == str2_len:
    cnt = 0
    for i in range(str1_len):
        if str1[i] != str2[i]:
            cnt += 1
    print(cnt)
else:
    cnt,tmp = 0,0
    for i in range(str2_len-str1_len+1):
        for d in range(i,i+str1_len):
            if str2[d]==str1[d-i]:
                tmp+=1
        cnt = max(tmp,cnt)
        tmp = 0
    print(str1_len-cnt)