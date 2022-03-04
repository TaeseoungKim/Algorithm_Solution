
def solution(phone_book):
    phone_book.sort(key=len)    
    phone_length = list(map(len, phone_book))
    list_length = len(phone_book)
    for i in range(list_length):
        for d in range(i+1,list_length):
            if phone_book[i][:phone_length[i]] == phone_book[d][:phone_length[i]]:
                return False
    return True
phone_book = ["119", "97674223", "1195524421"]	
print(solution(phone_book))
