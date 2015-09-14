t = int(raw_input())

def BiggerIsGreater(word):
    #print sorted(word)
    #print bool("".join(sorted(word)[::-1]) == word)
    if "".join(sorted(word)[::-1]) == word:
        return 'no answer'
    word_list = list(word)
    for i in range(len(word)-1)[::-1]:
        for j in range(i,len(word))[::-1]:
            if word_list[i] < word_list[j]:
                word_list = word_list[:i:] + [word_list.pop(j)] + sorted(word_list[i::])
                return "".join(word_list)

for case in range(t):
    w = raw_input()
    #print w
    print BiggerIsGreater(w)
