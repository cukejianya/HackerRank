def countSort(ar_pos, ar_str):
    pos_ar = [0 for x in range(100)]
    for x in ar_pos:
        pos_ar = [y+1 if x<=idx else y for idx, y in enumerate(pos_ar)]
    # print pos_ar
    ret_ar = []
    y = 0
    for idx, x in enumerate(pos_ar):
        for turns in range(y, x):
            jdx = ar_pos.index(idx)
            print 'jdx', jdx
            print ar_pos.pop(jdx)
            ret_ar.append(ar_str.pop(jdx))
        if x == len(ar):
            break
        y = x

    return " ".join(ret_ar)

n = int(raw_input())
ar = [raw_input().split() for x in range(n)]

ar_pos = [int(x[0]) for x in ar]
ar_str = ['-' if idx < n/2 else x[1] for idx, x in enumerate(ar)]
# print ar_pos
# print ar_str

print countSort(ar_pos, ar_str)
