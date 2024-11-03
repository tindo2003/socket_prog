from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [-1] * (len(edges) + 1)
        
        def find_parent(node, p):
            cur = node
            while p[cur] != -1:
                cur = p[cur]
            return cur
            
        for x, y in edges:
            x_parent = find_parent(x, parents)
            y_parent = find_parent(y, parents)
            if x_parent == y_parent: # detected cycle:
                return [x, y]
            else:
                parents[y_parent] = x_parent

        

        
