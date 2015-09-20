def insertion_sort(ar):
    counter = 0
    for idx, elm in enumerate(ar):
        if idx == 0:
            continue
        for jdx in range(0, idx)[::-1]:
            if ar[jdx] > ar[jdx+1]:
                ar[jdx+1] = ar[jdx]
                ar[jdx] = elm
                counter+=1
            else:
                break
    print counter
s = int(raw_input());
ar = [int(x) for x in raw_input().split()];
insertion_sort(ar)
