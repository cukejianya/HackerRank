def closest_numbers(ar):
    ret_ar = []
    x = ar[0] - ar[1]
    for idx, elm_x in enumerate(ar[:len(ar)-1]):
        for elm_y in ar[idx+1:]:
            num = abs(elm_x - elm_y)
            if num <= x:
                if num < x:
                    ret_ar = []
                    x = num
                ret_ar+=[elm_x, elm_y]


    return " ".join([str(x) for x in ret_ar])
s = int(raw_input());
ar = [int(x) for x in raw_input().split()];
print closest_numbers(ar)
