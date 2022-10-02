#가사 검색 문제

def solution(words, queries):
    answer = []
    
    # 검색키워드 대응
    words_len = []
    for word in words:
        words_len.append(len(word))
    
    for key in queries:
        key_len = len(key)
        start = 0 
        end = key_len-1
        cnt = 0
        all_q = 0
            
        if key[0] == '?' and key[key_len-1] == '?':
            all_q = 1
            for word_len in words_len:
                if word_len == key_len:
                    cnt += 1
                    
        elif key[0] == '?':
            for i in range(1,key_len):
                if key[i] != '?':
                    start = i
                    break
            for i in range(len(words)):
                
                if words_len[i] != key_len:
                    continue
                elif words[i][start:end+1] == key[start:]:
                    cnt += 1
        else: 
            for i in range(key_len-1,-1,-1):
                if key[i] != '?':
                    end = i
                    break
            for i in range(len(words)):
                
                if words_len[i] != key_len:
                    continue
                elif words[i][start:end+1] == key[:end+1]:
                    cnt += 1
        
        
        answer.append(cnt)
                    
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]


print(solution(words, queries))

