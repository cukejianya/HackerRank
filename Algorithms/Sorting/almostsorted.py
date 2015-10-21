def almostSorted(ar):
    swap = 0
    reverse = 0
    reverse_ar = []
    swap_idx = []
    swap_ar = []
    for idx, elm in enumerate(ar):
        print "swap", swap_ar
        print "reverse", reverse_ar
        print idx
        if idx < len(ar) - 1:
            other = ar[idx+1]
        else:
            other = elm + 1
        if elm > other:
            if reverse_ar and reverse == 1:
                reverse_ar.append(other)
            else:
                if reverse == 0:
                    reverse_ar.append(elm)
                    reverse_ar.append(other)
                else:
                    reverse = []
                reverse += 1
            if swap == 0:
                swap_idx = [idx,idx+1]
                swap += 1
            elif swap == 1:
                swap += 1
                switch = ar[swap_idx[0]]
                switch_next = ar[swap_idx[1]]
                if other < switch_next:
                    swap_ar = [switch, other]
                else:
                    swap_ar = []
            else:
                swap += 1
                swap_ar = []
        else:
            if reverse > 1:
                reverse_ar = []

    return [reverse_ar, swap_ar]

n = raw_input()
ar = [int(x) for x in raw_input().split()]

ret_ar = almostSorted(ar)
#print ret_ar

if ret_ar[1]:
    print "yes"
    print "swap"," ".join(str(x) for x in ret_ar[1])
elif ret_ar[0]:
    print "yes"
    if len(ret_ar[0]) == 2:
        print "swap",
    else:
        print "reverse",
    print ret_ar[0][::-1][0], ret_ar[0][0]
else:
    print "no"
