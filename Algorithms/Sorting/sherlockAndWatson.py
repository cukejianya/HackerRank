def sherlockAndWatson(N, K, ar, idx_ar):
    diff = K % N
    ar = ar[N-diff:]+ar[:N-diff]
    for  idx in idx_ar:
        print ar[idx]

input1 = raw_input().split()
N = int(input1[0])
K = int(input1[1])
Q = int(input1[2])
ar = [int(x) for x in raw_input().split()]
idx_ar = [int(raw_input()) for x in range(Q)]

sherlockAndWatson(N, K, ar, idx_ar)
