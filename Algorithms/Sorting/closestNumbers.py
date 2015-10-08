def quicksort(ar, front, end):
    pivot = ar[end-1]
    bound_idx = front;
    for idx in range(front, end):
        elm = ar[idx]
        if elm <= pivot:
            bigger_elm = ar[bound_idx]
            ar[bound_idx] = elm
            ar[idx] = bigger_elm
            bound_idx+=1
    if (end-front) < 2:
        return ar

    left = [front, bound_idx-1]
    ar = quicksort(ar, left[0], left[1])
    right = [bound_idx, end]
    ar = quicksort(ar, right[0], right[1])

    return ar

def closest_numbers(ar):
    ret_ar = []
    x = ar[0] - ar[1]
    for idx, elm_x in enumerate(ar[:len(ar)-1]):
        elm_y = ar[idx+1]
        num = abs(elm_x - elm_y)
        if num <= x:
            if num < x:
                ret_ar = []
                x = num
            ret_ar+=[elm_x, elm_y]

    return ret_ar

n = int(raw_input());
ar = [int(x) for x in raw_input().split()];
ar = quicksort(ar, 0, n)
ar = closest_numbers(ar)



print " ".join([str(x) for x in ar])
