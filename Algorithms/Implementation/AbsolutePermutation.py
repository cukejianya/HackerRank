def find_abs_permutation(n, k):
    set_dict = {}
    for i in range(1, n+1):
        higher_idx = k + i
        lower_idx = k - i
        if set_pos(higher_idx, set_dict, n)
            or set_pos(lower_idx, set_dict, n):
            return -1
    d = [set_dict.get(x) for x in range(1, n+1)]
    return d

def set_pos(pos, hash, n):
    if (pos < 1 or pos > n):
        return true
    if pos not in set_dict:
        set_dict[pos] = [i]
        return false
    elif len(set_dict[pos]) is 1:
        set_dict.append(pos)
        return false
    else:
        return true

T = int(raw_input());
for x in range(T):
    n, k = [int(x) for x in raw_input().split(' ')]
    print find_abs_permutation(n, k)
