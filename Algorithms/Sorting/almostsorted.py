def almostSorted(ar):
    reverse = 0
    swap = 0
    swap_ar = [0, len(ar)-1]
    reverse_ar = [0, 0]
    for idx, elm in enumerate(ar):
        if idx == 0:
            base = elm
            continue
        # print idx, elm
        prev = ar[idx - 1]
        if  prev > elm:
            if not swap:
                swap_ar = [idx, idx+1]
            else:
                swap_ar[1] = idx+1
            if not reverse:
                reverse_ar = [idx - 1]
            swap += 1
            reverse += 1
        else:
            if reverse and len(reverse_ar) == 1:
                reverse_ar.append(idx-1)
        #print swap_ar, swap
    if len(reverse_ar) == 1:
        reverse_ar.append(len(ar)-1)
    #print reverse
    #print reverse_ar

    if swap and swap < 3 and (swap > 1 or len(ar) == 2):
        return [True, "swap", " ".join(str(x) for x in swap_ar)]
    elif reverse and reverse  == reverse_ar[1] - reverse_ar[0] \
    and ar[reverse_ar[1]] > ar[reverse_ar[0] - 1]:
        return [True, "reverse", " ".join(str(ar[x]) for x in reverse_ar[::-1])]
    else:
        return [False]
n = raw_input()
ar = [int(x) for x in raw_input().split()]

ret_ar = almostSorted(ar)
#print ret_ar

if ret_ar[0]:
    print "yes"
    print ret_ar[1], ret_ar[2]
else:
    print "no"
