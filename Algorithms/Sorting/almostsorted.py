def almostSorted(ar):
    mini = 0
    maxi = 0
    ar = [-1]+ar+[1000001]
    n = len(ar)
    for idx, elm in enumerate(ar):
        #print idx, elm
        if idx == 0 or idx == n - 1:
            continue
        prev = ar[idx - 1]
        nxt = ar[idx + 1]
        if elm > prev and elm > nxt:
            idx_ar = [idx, 0]
            maxi += 1
        if elm < prev and elm < nxt:
            idx_ar[1] = idx
            mini += 1
    validate = (ar[idx_ar[1]+1] > ar[idx_ar[0]]);
    edgeCaseSwap = idx_ar[1]-idx_ar[0] == 1;

    if maxi == 0 and mini == 0:
        return [True, False]
    elif maxi == 1 and (mini == 2 or (validate and edgeCaseSwap)):
        return [True, "swap", " ".join(str(x) for x in idx_ar)]
    elif maxi == 1 and mini == 1 and validate:
        return [True, "reverse", " ".join(str(ar[x]) for x in idx_ar[::-1])]
    else:
        return [False]

n = raw_input()
ar = [int(x) for x in raw_input().split()]

ret_ar = almostSorted(ar)
#print ret_ar

if ret_ar[0]:
    print "yes"
    if ret_ar[1]:
        print ret_ar[1], ret_ar[2]
else:
    print "no"
