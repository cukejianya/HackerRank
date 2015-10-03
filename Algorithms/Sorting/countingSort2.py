def countSort(ar, n):
    ret_ar = [0 for x in range(100)]
    for x in ar:
        ret_ar[x]+=1
    ret_ar = [idx for idx, x in enumerate(ret_ar) for jdx in range(x)]
    return " ".join([str(x) for x in ret_ar])

n = int(raw_input())
ar = [int(x) for x in raw_input().split()]

print countSort(ar, n)
