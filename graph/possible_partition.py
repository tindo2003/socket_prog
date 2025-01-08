from collections import defaultdict
from typing import List
from collections import deque


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # OBJECTIVE: FIND IF WHETHER OR NOT GRAPH IS BIPARTITE
        visited = set()
        adj_lst = defaultdict(list)
        # make graph
        for x, y in dislikes:
            adj_lst[x].append(y)
            adj_lst[y].append(x)

        colored = defaultdict(list)

        # bfs function
        def bfs(cur_node) -> bool:
            root = cur_node
            cur_color = 0
            colored[root] = cur_color
            q = deque([root])
            while q:
                new_lst = deque([])
                cur_color = not cur_color
                for _ in range(len(q)):
                    cur = q.popleft()

                    for neighbor in adj_lst[cur]:
                        if neighbor in colored:
                            if colored[neighbor] == (not cur_color):
                                return False
                        else:
                            colored[neighbor] = cur_color
                            new_lst.append(neighbor)
                if not new_lst:
                    break
                q = new_lst
            return True

        # in case there are many forests.
        for idx in range(1, n + 1):
            if idx not in colored:
                if not bfs(idx):
                    return False

        return True
