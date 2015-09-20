def partition(ar, size):
    pivot = ar[0]
    sort_ar = [pivot]
    for idx in range(1, size):
        if ar[idx] < pivot:
            sort_ar = [ar[idx]] + sort_ar
        else:
            sort_ar = sort_ar + [ar[idx]]
    return " ".join([str(x) for x in sort_ar])

n = int(raw_input())
ar = [int(x) for x in raw_input().split()]
print partition(ar, n)
