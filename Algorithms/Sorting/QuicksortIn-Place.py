def quicksort(ar, front, end):
    # print end
    # print ar
    pivot = ar[end-1]
    # print 'pivot', pivot
    # print 'range', range(front, end)
    bound_idx = front;
    for idx in range(front, end):
        elm = ar[idx]
        if elm <= pivot:
            bigger_elm = ar[bound_idx]
            ar[bound_idx] = elm
            ar[idx] = bigger_elm
            bound_idx+=1
    # print "Before", ar
    if (end-front) < 2:
        # print "stop:...", ar
        return ar

    print " ".join([str(x) for x in ar])
    left = [front, bound_idx-1]
    # print "left", left
    ar = quicksort(ar, left[0], left[1])
    right = [bound_idx, end]
    # print "right", right
    ar = quicksort(ar, right[0], right[1])

    return ar

n = int(raw_input())
ar = [int(x) for x in raw_input().split()]

quicksort(ar, 0, n)
