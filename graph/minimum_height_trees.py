from typing import List 
from collections import deque, defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_lst = defaultdict(list)
        if not edges: return [0]
        for x, y in edges:
            adj_lst[x].append(y)
            adj_lst[y].append(x)
        
        self.depth = 0 
        # self.left_end and self.right_end represents the two endpoints of the longest path in a tree
        self.left_end = -1
        self.right_end = -1
        self.visited = set([0])
        def dfs(cur, cur_depth, left):
            if cur_depth > self.depth:
                self.depth = cur_depth
                if left:
                    self.left_end = cur
                else:
                    self.right_end = cur
            for neighbor in adj_lst[cur]:
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    dfs(neighbor, cur_depth + 1, left)
        dfs(0, 0, True)
        self.depth = 0
        self.visited = set([self.left_end])
        dfs(self.left_end, 0, False)

        parents = {}
        q = deque([self.left_end])
        parents[self.left_end] = None
        while q:
            cur = q.popleft()
            for neighbor in adj_lst[cur]:
                if neighbor not in parents:
                    parents[neighbor] = cur 
                    q.append(neighbor)
        path = deque([cur])
        cur = self.right_end 
        while parents[cur] != None:
            cur = parents[cur]
            path.appendleft(cur)
        length = len(path)
        
        # we know that there will be at most 2 roots that creates the minimum height tree
        if length % 2 == 0:
            return [path[length // 2], path[length // 2 - 1]]
        else:
            return [path[length // 2]]