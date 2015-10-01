def partition(ar):
    pivot = [ar[0]]
    size = len(ar)
    lh = []
    rh = []
    for idx in range(1,  size):
        if ar[idx] > pivot[0]:
            rh.append(ar[idx])
        else:
            lh.append(ar[idx])
    if len(lh) > 1:
        lh = partition(lh)
    if len(rh) > 1:
        rh = partition(rh)
    sorted_ar = lh+pivot+rh
    print " ".join([str(x) for x in sorted_ar])
    return sorted_ar
n = int(raw_input())
ar = [int(x) for x in raw_input().split()]
partition(ar)
