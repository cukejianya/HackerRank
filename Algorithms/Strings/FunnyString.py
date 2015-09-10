T = int(raw_input())

def FunnyString():
    S = raw_input()
    R = S[::-1]
    for idx in range(len(S))[1::]:
        s_diff = ord(S[idx]) - ord(S[idx-1])
        r_diff = ord(R[idx]) - ord(R[idx-1])
        if abs(s_diff != r_diff):
            return 'Not Funny'
    return 'Funny'

for i in range(T):
    print FunnyString()
