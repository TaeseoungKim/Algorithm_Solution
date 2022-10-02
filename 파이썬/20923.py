n, m = map(int,input().split())

do_list = []
su_list = []

for i in range(n):    
    tmp_do, tmp_su = map(int,input().split())
    do_list.append(tmp_do)
    su_list.append(tmp_su)

i=0
is_turn = 0
is_empty = 0
do_ground = []
su_ground = []

do_open = 0
su_open = 0


#while i < m :
for i in range(m):

    if is_turn == 0 :
        do_open = do_list.pop()
        do_ground.append(do_open)
        is_turn = 1
    else :
        su_open = su_list.pop()
        su_ground.append(su_open)
        is_turn = 0

    if len(do_list) == 0 :
        print("su")
        exit(0)
    elif len(su_list) == 0 :
        print("do")
        exit(0)


    if do_open + su_open == 5 and do_open != 0 and su_open != 0 :
        do_ground.extend(su_list) # 상대 그라운드에 있는 카드 더미를 뒤집어 자신의 덱 아래로 그대로 합친 후 
        su_ground.extend(do_ground) # 자신의 그라운드에 있는 카드 더미 역시 뒤집어 자신의 덱 아래로 그대로 가져와 합친다.
        su_list = su_ground
        do_ground = []
        su_ground = []
        # i += 1

    

    if do_open == 5 or su_open == 5 :
        su_ground.extend(do_list) # 상대 그라운드에 있는 카드 더미를 뒤집어 자신의 덱 아래로 그대로 합친 후 
        do_ground.extend(su_ground) # 자신의 그라운드에 있는 카드 더미 역시 뒤집어 자신의 덱 아래로 그대로 가져와 합친다.
        do_list = do_ground
        do_ground = []
        su_ground = []
    

len_do = len(do_list)
len_su = len(su_list)

#print("do = %d , su = %d"%(len_do,len_su))

if len_do == len_su :
    print("dosu")
elif len_do > len_su :
    print("do")
elif len_su > len_do :
    print("su")

exit(0);