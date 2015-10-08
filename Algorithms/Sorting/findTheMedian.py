def median(ar, front, end):
    pivot = ar[end-1]
    bound_idx = front;
    for idx in range(front, end):
        elm = ar[idx]

        if elm <= pivot:
            bigger_elm = ar[bound_idx]
            ar[bound_idx] = elm
            ar[idx] = bigger_elm
            bound_idx+=1
            # print ar, front, end, "bound", bound_idx, "diff", end - front

    if (end-front) < 2:
        if bound_idx > len(ar)//2:
            return ar[len(ar)//2]
        return ar

    left = [front, bound_idx-1]
    if type(ar) is int:
        return ar
    else:
        ar = median(ar, left[0], left[1])

    right = [bound_idx, end]
    if type(ar) is int:
        return ar
    else:
        ar = median(ar, right[0], right[1])

    return ar

n = int(raw_input());
ar = [int(x) for x in raw_input().split()];
print median(ar, 0, n)
