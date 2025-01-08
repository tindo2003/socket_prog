from typing import (
    List,
)
from collections import defaultdict


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        parents = [i for i in range(n)]

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

        def dfs(cur):
            for neighbor in adj_lst[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for x, y in edges:
            if not union(x, y):
                return False

        visited = set([0])
        adj_lst = defaultdict(list)
        for x, y in edges:
            adj_lst[x].append(y)
            adj_lst[y].append(x)

        dfs(0)
        return len(visited) == n
