def closest_numbers(ar):
    ret_ar = []
    x = 0
    for idx, elm in enumerate(ar):
        if idx == 0:
            continue
        for jdx in range(0, idx)[::-1]:
            number = abs(elm - ar[idx])
            if not x and not ret_ar:
                x = number
            if number <= x and not number == 0:
                if number < x:
                    ret_ar = []
                ret_ar+=[elm, ar[idx]]
    return " ".join([str(x) for x in ret_ar])
s = int(raw_input());
ar = [int(x) for x in raw_input().split()];
print closest_numbers(ar)
