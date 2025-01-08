from typing import List
from collections import defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # OBJECTIVE: remove n-1 from each n-length connected component
        # find connected component via union find
        n = len(stones)
        parents = [i for i in range(n)]

        def join(child, parent):
            parent_root = find(parent)
            child_root = find(child)
            parents[child_root] = parent_root

        def find(cur):
            while parents[cur] != cur:
                cur = parents[cur]
            return cur

        for i in range(n):
            for j in range(i + 1, n):
                r, c = stones[i]
                r1, c2 = stones[j]
                if r == r1 or c == c2:
                    join(i, j)

        group = defaultdict(list)
        for idx in range(n):
            root = find(idx)
            group[root].append(idx)

        res = 0
        for lst in group.values():
            res += len(lst) - 1
        return res
