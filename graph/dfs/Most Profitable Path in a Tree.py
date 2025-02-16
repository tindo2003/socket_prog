from typing import List
from collections import defaultdict
from math import inf


class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        adj_lst = defaultdict(list)
        for x, y in edges:
            adj_lst[x].append(y)
            adj_lst[y].append(x)

        q = [bob]
        time = defaultdict(int)  # node -> time
        time[bob] = 0
        visited = set([bob])

        def dfs_bob(cur_node, cur_time):
            if cur_node == 0:
                time[cur_node] = cur_time
                return True
            if not cur_node:
                return False
            for neighbor in adj_lst[cur_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if dfs_bob(neighbor, cur_time + 1):
                        time[cur_node] = cur_time
                        return True
            return False

        dfs_bob(bob, 0)

        visited = set([0])

        def dfs_alice(cur_node, cur_time):
            max_val = -inf
            for neighbor in adj_lst[cur_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    tmp = dfs_alice(neighbor, cur_time + 1)

                    max_val = max(max_val, tmp)

            cur_reward = amount[cur_node]
            if cur_node in time:
                if cur_time == time[cur_node]:
                    cur_reward = amount[cur_node] / 2
                elif cur_time < time[cur_node]:
                    cur_reward = amount[cur_node]
                else:
                    cur_reward = 0
            if max_val != -inf:
                return cur_reward + max_val
            else:
                return cur_reward

        return int(dfs_alice(0, 0))
