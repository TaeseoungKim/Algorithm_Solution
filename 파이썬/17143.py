import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
if M==0:
    print(0)
else:
    sharkDict = dict()
    for i in range(M):
        r, c, s, d, z = map(int, input().split())
        sharkDict[(r-1,c-1)] = [(r-1, c-1, s, d, z)]

    def sharkMove(shark):
        row, column, speed, moveDir, size = shark
        originSpeed = speed
        while speed != 0:
            if moveDir==1:
                if row > speed:
                    row -= speed
                    speed = 0
                else:
                    speed -= row
                    row = 0
                    moveDir = 2
            
            if moveDir==2:
                if R > row+speed:
                    row += speed
                    speed = 0
                else:
                    speed -= (R-1-row)
                    row = R-1
                    moveDir = 1
                    
                    
            if moveDir==3:
                if C > column+speed:
                    column += speed
                    speed = 0
                else:
                    speed -= (C-1-column)
                    column = C-1
                    moveDir = 4
                    
            if moveDir==4:
                if column > speed:
                    column -= speed
                    speed = 0
                else:
                    speed -= column
                    column = 0
                    moveDir = 3
        return (row, column, originSpeed, moveDir, size)

    answer = 0
    for i in range(C):
        # 1. 낚시 단계
        curShark = (R,0)
        tRow, tCol = R,C
        for key in sharkDict.keys():
            row, column, speed, moveDir, size = sharkDict[key][0]
            if column==i and row < curShark[0]:
                curShark = (row,size)
                tRow, tCol = row, column
                
        if tRow!=R and tCol!=C:
            del sharkDict[(tRow,tCol)]
            answer += curShark[1]

        # 2. 상어 이동 단계
        tempSharkDict = dict()
        for key in sharkDict.keys():
            row, column, speed, moveDir, size = sharkMove(sharkDict[key][0]) 
            if (row,column) in tempSharkDict:
                tempSharkDict[(row,column)].append((row, column, speed, moveDir, size))
            else:
                tempSharkDict[(row,column)] = [(row, column, speed, moveDir, size)]
        sharkDict = tempSharkDict

        for key in sharkDict.keys():
            sharkDict[key] = sorted(sharkDict[key],key=lambda x: -x[4])

    print(answer)


