def quicksort(ar, front, end):
    pivot = ar[len(ar)-1]
    bound_idx = 0;
    for idx range(front, end):
        elm = ar[idx]
        if elm <= pivot:
            bigger_elm = ar[bound_idx]
            ar[bound_idx] = elm
            ar[idx] = bigger_elm
            bound_idx+=1
     print "Before", ar
     if (end-front) < 2:
         return ar

    print " ".join([str(x) for x in ar)
    left = [front, bound_idx-1]
    ar = quicksort(ar, left[0], left[1])
    right = [bound_idx, end]
    ar = quicksort(ar, right[0], right[1])






    # left = ar[:bound_idx-1:]
    # right = ar[bound_idx::]
    # right_old = [pivot] + right + right_old
    # print "--Right_old...", right_old
    # print "--Right...", right
    # print "Left-before...", left
    # print "Left_old-before...", left_old
    # ar = quicksort(left, left_old, right_old)
    # print "After: ", ar
    #
    # left = ar[:bound_idx-1:]
    # left_old = left_old + left + [pivot]
    # print "--Left...", left
    # print "--Left_old...", left_old
    # ar = quicksort(right, left_old, right_old)


n = int(raw_input())
ar = [int(x) for x in raw_input().split()]

quicksort(ar, [], [])
