from typing import List 
from collections import defaultdict
from math import inf

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_adj_lst = defaultdict(list)
        for x, y in redEdges:
            red_adj_lst[x].append(y)
        blue_adj_lst = defaultdict(list)
        for x, y in blueEdges:
            blue_adj_lst[x].append(y)
        
        res = [inf] * n
        # red = 0, blue = 1
        res[0] = 0
        q = [(0,0,0), (0,1,0)]
        visited = set([(0,0),(0,1)])
        while q:
            cur_node, last_color, dst = q.pop(0)
            if last_color == 0:
                for new_node in blue_adj_lst[cur_node]:
                    if (new_node, 1) not in visited:
                        q.append((new_node, 1, dst + 1))
                        visited.add((new_node, 1))
                        res[new_node] = min(res[new_node], dst + 1)
            else:
                for new_node in red_adj_lst[cur_node]:
                    if (new_node, 0) not in visited:
                        q.append((new_node, 0, dst + 1))
                        visited.add((new_node, 0))
                        res[new_node] = min(res[new_node], dst + 1)
        return [-1 if item == inf else item for item in res]
                
            
