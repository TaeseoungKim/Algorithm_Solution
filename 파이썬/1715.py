import sys
input = sys.stdin.readline

n =int(input())
card_list = [int(input()) for _ in range(n)]
result_list = []
card_list.sort()
sum_card = 0

result = 0

for card in card_list:
    sum_card += card
    result_list.append(sum_card)
    
result_list.pop(0)
print(result_list)
print(sum(result_list))