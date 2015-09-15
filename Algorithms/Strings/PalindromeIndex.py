T = int(raw_input())

def palindrome_index(word):
    if word == word[::-1]:
        return -1
    for idx in range(len(word)//2):
        front = idx
        back = len(word) - 1 - idx
        if not word[front] == word[back]:
            if word[front] == word[back-1] and word[front+1] == word[back-2]:
                return back
            else:
                return front

for case in range(T):
    S = raw_input()
    print palindrome_index(S)
