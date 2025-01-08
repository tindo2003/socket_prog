from typing import List
from math import inf


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        max_val = -inf
        for a, b in edges:
            max_val = max(max_val, a)
            max_val = max(max_val, b)
        parents = [i for i in range(max_val + 1)]

        # if parent and child have the same parent, then we have a cycle
        def union(child, parent) -> bool:
            child_parent = find(child)
            parent_parent = find(parent)
            if child_parent == parent_parent:
                return False
            parents[child_parent] = parent_parent
            return True

        def find(cur):
            while parents[cur] != cur:
                cur = parents[cur]
            return cur

        for x, y in edges:
            if not union(x, y):
                return [x, y]
