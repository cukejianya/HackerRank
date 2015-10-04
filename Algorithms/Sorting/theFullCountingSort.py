def countSort(ar_pos, ar_str):
    ret_ar = ['' for x in range(100)]
    for idx, x in enumerate(ar_pos):
        ret_ar[x] = ar_str[idx] if not ret_ar[x] else ret_ar[x] + ar_str[idx]
    return " ".join(ret_ar)

n = int(raw_input())
ar_pos = []
ar_str = []

for turn in range(n):
    io_ar = raw_input().split()
    ar_pos.append(int(io_ar[0]))
    if turn < n/2:
        ar_str.append('-')
    else:
        ar_str.append(io_ar[1])

print countSort(ar_pos, ar_str)
