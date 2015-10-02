def quicksort(ar, front, end):
    if (end-front) < 2:
        return ar
        
    pivot = ar[end-1]
    bound_idx = front;
    for idx in range(front, end):
        elm = ar[idx]
        if elm <= pivot:
            global quick
            quick+=1
            bigger_elm = ar[bound_idx]
            ar[bound_idx] = elm
            ar[idx] = bigger_elm
            bound_idx+=1

    left = [front, bound_idx-1]
    ar = quicksort(ar, left[0], left[1])
    right = [bound_idx, end]
    ar = quicksort(ar, right[0], right[1])

    return ar

def insertion_sort(ar):
    for idx, elm in enumerate(ar):
        if idx == 0:
            continue
        for jdx in range(0, idx)[::-1]:
            if ar[jdx] > ar[jdx+1]:
                global insert
                insert+=1
                ar[jdx+1] = ar[jdx]
                ar[jdx] = elm
            else:
                break

n = int(raw_input())
ar = [int(x) for x in raw_input().split()]
other_ar = [x for x in ar]
quick, insert = 0, 0

quicksort(ar, 0, n)
insertion_sort(other_ar)

print insert - quick
