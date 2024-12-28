from collections import defaultdict


class Result:
    def findMaximumSum(
        self,
        tree_node: int,
        tree_from: list[int],
        tree_to: list[int],
        weight: list[int],
    ) -> int:
        adj_lst = defaultdict(list)
        for node1, node2 in zip(tree_from, tree_to):
            adj_lst[node1].append(node2)
            adj_lst[node2].append(node1)

        def dfs(cur_node: int, parent) -> int:
            unpicked = 0
            for neighbor in adj_lst[cur_node]:
                if neighbor != parent:
                    unpicked += dfs(neighbor, cur_node)
            return max(weight[cur_node - 1], unpicked)

        return dfs(1)


class Solution:
    sol = Result()
    tree_nodes = 3
    tree_from = [1, 1]
    tree_to = [2, 3]
    weight = [4, 2, 1]
    ans = sol.findMaximumSum(tree_nodes, tree_from, tree_to, weight)
    print(ans)
