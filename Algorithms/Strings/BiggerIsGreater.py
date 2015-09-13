t = int(raw_input())

def BiggerIsFreater(word):
    if "".join(sorted(word)[::-1]) == word:
        return 'no answer'
    word_list = list(word)
    for i in range(len(word))[::-1]:
        current_char = word_list[i]
        for j in range(len(i+1,word))[::-1]:
            if current_char > word_list[j]:
                word_list = word_list[0:j:] + [current_char]


def switchWords(wordarray, letter):
