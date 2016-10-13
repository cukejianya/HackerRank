import math

def find_abs_permutation(n, k):
    set_dict = {}
    for i in range(1, n+1):
        higher_idx = i + k
        lower_idx = i - k
        set_pos(higher_idx, set_dict, n, i)
        set_pos(lower_idx, set_dict, n, i)
        if len(set_dict) not n:
            return -1
    return set_dict

def set_pos(pos, hash, n, i):
    if (pos < 1 or pos > n):
        return
    if pos not in hash:
        hash[pos] = [i]
    else:
        hash[pos].append(pos)

def check_hash(hash, n):
    seen_nums = set([])
    for i in range(1, math.ceil(n/float(2))+1):
        front_list = set_dict[i]
        end_list = set_dict[n + 1 - i]
        if len(front_list) is 1 front_list[0] not in seen_nums:
            seen_nums.add(front_list)
        if len(end_list) is 1:
            if end_list[n + 1 - i][0] not in seen_nums:
                seen_nums.add(end_list[0])
            else:
                return -1
        else:
            




T = int(raw_input());
for x in range(T):
    n, k = [int(x) for x in raw_input().split(' ')]
    print find_abs_permutation(n, k)
