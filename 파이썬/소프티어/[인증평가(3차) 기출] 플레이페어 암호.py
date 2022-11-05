import sys
from collections import deque
input = sys.stdin.readline

msg = input().rstrip()
PF_key = input().rstrip()
# msg = "HELLOWORLD"
# PF_key = "PLAYFAIRCIPHERKEY"

PF_dict = dict()
PF_deque = deque()


for c in PF_key:
    if c in PF_dict:
        continue
    else:
        PF_dict[c] = True
        PF_deque.append(c)

Alpha = deque(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

key_board = [[] for i in range(5)]

for i in range(5):
    for d in range(5):
        if PF_deque:
            key_board[i].append(PF_deque.popleft())
        else:
            while Alpha:
                Tmp = Alpha.popleft()
                if Tmp in PF_dict:
                    continue
                else:
                    key_board[i].append(Tmp)
                    break

idx = 0

while idx <= len(msg)-1:
    if msg[idx] == 'X' and msg[idx] == msg[idx+1]:
        msg = msg[:idx+1]+'Q'+msg[idx+1:]
    elif msg[idx] == msg[idx+1]:
        msg = msg[:idx+1]+'X'+msg[idx+1:]
    if idx+2 == len(msg)-1:
        msg = msg[:]+'X'

    idx += 2

idx = 0
newMsg = ""
while idx <= len(msg)-1:
    Left, Right = (0, 0), (0, 0)

    for i in range(5):
        for d in range(5):
            if key_board[i][d] == msg[idx]:
                Left = (i, d)
            if key_board[i][d] == msg[idx+1]:
                Right = (i, d)

    if Left[0] != Right[0] and Left[1] != Right[1]:
        newMsg += key_board[Left[0]][Right[1]]
        newMsg += key_board[Right[0]][Left[1]]

    elif Left[0] == Right[0] and Left[1] == Right[1]:
        newMsg += key_board[Left[0]][Left[1]+1]
        newMsg += key_board[Left[0]][Left[1]+1]

    elif Left[0] == Right[0]:
        if Left[1] == 4:
            newMsg += key_board[Left[0]][0]
        else:
            newMsg += key_board[Left[0]][Left[1]+1]

        if Right[1] == 4:
            newMsg += key_board[Right[0]][0]
        else:
            newMsg += key_board[Right[0]][Right[1]+1]

    elif Left[1] == Right[1]:
        if Left[0] == 4:
            newMsg += key_board[0][Left[1]]
        else:
            newMsg += key_board[Left[0]+1][Left[1]]

        if Right[0] == 4:
            newMsg += key_board[0][Right[1]]
        else:
            newMsg += key_board[Right[0]+1][Right[1]]

    idx += 2


print(newMsg)
