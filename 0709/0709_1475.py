"""

다솜이는 은진이의 옆집에 새로 이사왔다. 
다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.
다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 
한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다.
 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오.
  (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

"""

number = input()
cnt = len(number)
number = int(number)
tmp_list = []
ten = 10    
is_six_nine = 0 

if(number > 1000000 or 0 > number) :
    print("잘못된 숫자입니다.")
    exit(0)

for i in range(cnt):
    
    if i == 0 :
        remainder = number % 10
    else:
        remainder = number % (10**(i+1)) // 10**i
    if remainder == 6 or remainder ==9 :
        is_six_nine += 1
    tmp_list.append(remainder)

max_same = 0


            

for i in range(cnt):

    tmp_same = 0
    for a in range(cnt):
        if tmp_list[i] == tmp_list[a] and i != a :
            if(tmp_list[i] != 6 and tmp_list[i] != 9):
                tmp_same += 1
             
    if tmp_same > max_same :
        max_same = tmp_same


if is_six_nine > 2 :
    if max_same < is_six_nine//2 :
        max_same = is_six_nine//2
    elif max_same < is_six_nine//2 + 1 :
        max_same = is_six_nine//2 + 1




print(is_six_nine)
print(tmp_list) 
print(max_same)   
