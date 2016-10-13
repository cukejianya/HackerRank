def find_abs_permutation(n, k):
    seen_list = []
    if k > n/2:
        return -1

    for pos in range(1, n+1):
        higher = pos + k
        lower = pos - k

        if higher > n:
            seen_list.append(lower)
        elif lower < 1:
            seen_list.append(higher)
        elif lower < 1 and higher > n:
            return -1
        elif lower in seen_list:
            seen_list.append(higher)
        else:
            seen_list.append(lower)

    if len(set(seen_list)) < n:
        return -1

    return ' '.join(str(num) for num in seen_list)


T = int(raw_input());
for x in range(T):
    n, k = [int(x) for x in raw_input().split(' ')]
    print find_abs_permutation(n, k)
