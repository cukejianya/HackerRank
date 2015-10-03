def countSort(ar):
    pos_ar = [0 for x in range(100)]
    for x in ar:
        pos_ar = [y+1 if x[0]<=idx else y for idx, y in enumerate(pos_ar)]
    for idx, x in enumerate(pos_ar):
        for y in ar:
            idx = y[1]
            elm = y[0]


    return " ".join([str(x) for x in ret_ar])

n = int(raw_input())
ar = [int(raw_input().split() for x in range(n)]

print countSort(ar)
