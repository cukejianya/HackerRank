s = int(raw_input())
ar = [int(x) for x in raw_input().split()]

number = ar[len(ar)-1]
for i in range(s-1)[::-1]:
    if ar[i] > number:
        ar[i+1] = ar[i]
    else:
        ar[i+1] = number
        break
    print ' '.join([str(x) for x in ar])
    if i == 0:
            ar[0] = number

print ' '.join([str(x) for x in ar])
