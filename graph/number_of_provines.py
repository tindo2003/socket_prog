from typing import List
class Solution:
    def findCircleNum(self, isConnected) -> int:
        N = len(isConnected)
        visited = [False] * N
        ans = 0
        def dfs(node):
            visited[node] = True 
            for new_node in range(N):
                if new_node != node and not visited[new_node] and isConnected[node][new_node] == 1: 
                    dfs(new_node)
        for node in range(N):
            if not visited[node]:
                ans += 1
                dfs(node)
        return ans  