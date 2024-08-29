from typing import List 
from collections import defaultdict
import math 
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_lst = defaultdict(dict)
        for (x, y), wt in zip(edges, succProb):
            adj_lst[x][y] = wt
            adj_lst[y][x] = wt
        distances = {node: float('infinity') for node in adj_lst}
        prev = {node: None for node in adj_lst}
        distances[start_node] = 0
        visited = set()  

        pq = [(0, start_node)]
        while pq:
            cur_wt, cur_node = heapq.heappop(pq)

            if cur_node == end_node:
                break

            if cur_node in visited:
                continue 
            visited.add(cur_node)

            for neighbor, wt in adj_lst[cur_node].items():
                if neighbor in visited: continue 
                wt = -math.log(wt)
                dist = cur_wt + wt 
                if distances[neighbor] > dist:
                    distances[neighbor] = dist 
                    prev[neighbor] = cur_node
                    heapq.heappush(pq, (dist, neighbor))

        if end_node not in adj_lst or distances[end_node] == inf:
            return 0
        tmp_node = end_node
        res = 1
        while prev[tmp_node]:
            parent = prev[tmp_node] 
            res *= adj_lst[tmp_node][parent]
            tmp_node = parent
        return res


        
