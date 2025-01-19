from collections import defaultdict
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degrees = defaultdict(int)
        adj_lst = defaultdict(list)
        for x, y in roads:
            degrees[x] += 1
            degrees[y] += 1
            adj_lst[x].append(y)
            adj_lst[y].append(x)

        res = 0
        key_lst = list(degrees.keys())
        N = len(key_lst)
        for i in range(N):
            for j in range(N):
                node1 = key_lst[i]
                node2 = key_lst[j]
                if node1 != node2:
                    tmp = degrees[node1] + degrees[node2]
                    if node1 in adj_lst[node2]:
                        tmp -= 1
                    res = max(res, tmp)
        return res
