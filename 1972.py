import sys
input = sys.stdin.readline
board = []

while True:
    tmp = input().strip()
    if tmp=="*":
        break
    board.append(tmp)

def check(word):
    
    wordLen = len(word)
    for i in range(1,wordLen-1):
        dic = dict()
        for d in range(wordLen-i):
            if dic.get(word[d]+word[d+i])==None:
                dic[word[d]+word[d+i]]=1
            else:
                return False
    return True

for word in board:
    if check(word):
        print(word,"is surprising.")
    else:
        print(word,"is NOT surprising.")

