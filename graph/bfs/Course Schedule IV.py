class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        adj_lst = defaultdict(list)
        for i, j in prerequisites:
            adj_lst[i].append(j)
        is_reachable = [[0] * numCourses for _ in range(numCourses)]

        def bfs(start):
            q = [start]
            while q:
                cur_node = q.pop(0)
                is_reachable[start][cur_node] = True
                for neighbor in adj_lst[cur_node]:
                    if not is_reachable[start][neighbor]:
                        q.append(neighbor)

        for node in range(numCourses):
            bfs(node)

        res = []
        for fr, to in queries:
            res.append(bool(is_reachable[fr][to]))
        return res
