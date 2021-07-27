number = input()
lst = []

for i in number:
    lst.append(i)

len_lst = len(lst)

six_nine = 0
final_max = 0

for a in range(len_lst):
    max_cnt = 1
    for b in range(len_lst):
        
        if a == b :
            continue
        elif lst[a] == '6' or lst[a] == '9': 
            six_nine += 1
            break
        elif lst[a] == lst[b] :
            max_cnt += 1

    if max_cnt >= final_max :
        final_max = max_cnt

if six_nine % 2 == 0 :
    six_nine = six_nine // 2
else :
    six_nine = six_nine // 2 + 1

if six_nine >= final_max :
    print(six_nine)
else :
    print(final_max)


