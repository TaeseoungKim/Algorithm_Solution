
alphabet = set(["c=","c-","dz=","d-","lj","s=","nj","z="])
word = input()
tmp_word = ""
answer = 0
word_len = len(word)
for i in range(word_len):
        answer += 1
        if i == 0:
            continue
        elif word[i-1] + word[i] in alphabet:
            answer -= 1
        elif i != word_len-1 and  (word[i-1] + word[i] + word[i+1] == "dz="):

            answer -= 1
            i += 1
print(answer)