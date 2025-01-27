class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Most Stones Removed with Same Row or Column on steroid
        n = len(grid)
        m = len(grid[0])

        def union(child, parent):
            child_parent = find(child)
            parent_parent = find(parent)
            parents[child_parent] = parent_parent

        def find(cur):
            while parents[cur] != cur:
                cur = parents[cur]
            return cur

        my_nodes = []
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    my_nodes.append((r, c))
        k = len(my_nodes)
        parents = [i for i in range(k)]

        for i in range(k):
            for j in range(i + 1, k):
                r, c = my_nodes[i]
                r1, c2 = my_nodes[j]
                if r == r1 or c == c2:
                    union(i, j)

        groups = defaultdict(list)
        for idx in range(len(parents)):
            group = find(idx)
            groups[group].append(my_nodes[idx])

        res = 0
        for group, lst in groups.items():
            if len(lst) > 1:
                res += len(lst)

        return res
