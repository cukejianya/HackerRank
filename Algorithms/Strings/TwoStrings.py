T = int(raw_input())

def TwoStrings(str_A, str_B):
    smallest = min(len(str_A), len(str_B))
    if smallest == len(str_A):
        for elm in str_A:
            if elm in str_B:
                return 'YES'
    else:
        for elm in str_B:
            if elm in str_A:
                return 'YES'
    return 'NO'


for case in range(T):
    A = raw_input()
    B = raw_input()
    A = list(set(A))
    B = list(set(B))
    print TwoStrings(A, B)
