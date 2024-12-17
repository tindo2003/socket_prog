#
import heapq


def getGreatestElements(arr, k):
    # Write your code here
    h = []
    for i in range(k):
        heapq.heappush(h, arr[i])
        if len(h) > k:
            heapq.heappop(h)
    res = []
    res.append(h[0])
    for idx in range(k, len(arr)):
        heapq.heappush(h, arr[idx])
        if len(h) > k:
            heapq.heappop(h)
        res.append(h[0])
    return res
