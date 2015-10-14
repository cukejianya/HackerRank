def almostSorted(ar):
    swap = 0
    reverse = 0
    reverse_ar = []
    swap_idx = []
    for idx, elm in enumerate(ar):
        other = ar[idx+1]
        if elm > other:
            if reverse > 0:
                reverse_ar = []
            else:
                reverse_ar.append(elm) 
                reverse += 1
            if swap == 0:
                swap_idx = [idx,idx+1]
                swap += 1
        else:
            if reverse > 0:
                reverse_ar.append(elm)



n = raw_input()
ar [int(x) for x in raw_input().split()]