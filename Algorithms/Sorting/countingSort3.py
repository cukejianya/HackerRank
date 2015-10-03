def countSort(ar):
    ret_ar = [0 for x in range(100)]
    for x in ar:
        ret_ar = [y+1 if x<=idx else y for idx, y in enumerate(ret_ar)]
    return " ".join([str(x) for x in ret_ar])

n = int(raw_input())
ar = [int(raw_input().split()[0]) for x in range(n)]

print countSort(ar)
