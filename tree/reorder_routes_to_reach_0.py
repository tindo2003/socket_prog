from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        undirected_graph = defaultdict(list)
        for x, y in connections:
            undirected_graph[x].append((y, 1))
            undirected_graph[y].append((x, 0))
        res = 0
        def dfs(cur, parent):
            nonlocal res
            for (neighbor, sign) in undirected_graph[cur]:
                if neighbor != parent:
                    res += sign
                    dfs(neighbor, cur)
        dfs(0, -1)
        return res