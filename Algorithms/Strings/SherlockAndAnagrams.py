import math

T = int(raw_input())
def map_reduce(array):
    total = 0
    for elm in array:
        total += nCr(elm, 2)
    return total

def nCr(num, groupsize):
    f = math.factorial
    if num < groupsize:
        return 0
    return f(num)/f(groupsize)/f(num-groupsize)

def SherlockAndAnagrams(word):
    anagrams_dict = {}
    for i in range(len(word)):
        for j in range(i+1,len(word)+1):
            anagram = ''.join(sorted(word[i:j:]))
            if anagram in anagrams_dict:
                anagrams_dict[anagram] += 1
            else:
                anagrams_dict[anagram] = 0
    return map_reduce(anagrams_dict.values())

for case in range(T):
    S = raw_input()
    print SherlockAndAnagrams(S)
