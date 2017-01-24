from heapq import heappop, heappush

input_list = raw_input().split()

def findMinMax(arr):
    heap = []
    minVal = 0
    maxVal = 0

    for x in arr:
        heappush(heap, int(x))

    for i in range(len(arr)):
        x = heappop(heap)
        if i is not 0:
            maxVal = maxVal + x
        if i is not len(arr) - 1:
            minVal = minVal + x

    print minVal, maxVal

findMinMax(input_list)
