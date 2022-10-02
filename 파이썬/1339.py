import sys
input = sys.stdin.readline

n = int(input())

word_list = []
alphabet_value = {'A':-1, 'B':-1, 'C':-1, 'D':-1, 'E':-1, 'F':-1, 'G':-1, 'H':-1, 'I':-1, 'J':-1, 'K':-1, 'L':-1, 'M':-1, 'N':-1, 'O':-1, 'P':-1, 'Q':-1, 'R':-1, 'S':-1, 'T':-1, 'U':-1, 'V':-1, 'W':-1, 'X':-1, 'Y':-1, 'Z':-1}

# 아 알겟다... 각 자릿 수 마다...
# 뭐랄까 .. . . . . . ... . . . . . . . . .10000 , 110000, ㅇㅈㄹ로 해놓은 다음 .......................... 가장 가중치가 높은거 부터? 주는거야

for _ in range(n):
    word_list.append(input())

cnt = 9
result = 0

for word in word_list:
    word_length = len(word)-1
    for alphabet in range(word_length):
        if alphabet_value[word[alphabet]] == -1:
            alphabet_value[word[alphabet]] = cnt
            cnt-=1
        word_length -= 1
        print("value: ",alphabet_value[word[alphabet]]*10**word_length )
        result += alphabet_value[word[alphabet]]*10**word_length


print(result)