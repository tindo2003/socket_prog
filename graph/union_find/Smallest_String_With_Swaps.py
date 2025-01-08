from typing import List
from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        parents = [i for i in range(N)]
        rank = [1] * N

        def find(child):
            cur = child
            while parents[cur] != cur:
                cur = parents[cur]
            return cur

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parents[rootY] = rootX
                elif rank[rootY] > rank[rootX]:
                    parents[rootX] = rootY
                else:
                    parents[rootY] = rootX
                    rank[rootX] = rootY

        for x, y in pairs:
            union(x, y)

        groups_i = defaultdict(list)
        groups_char = defaultdict(list)
        for idx in range(N):
            group = find(idx)
            groups_i[group].append(idx)
            groups_char[group].append(s[idx])

        res = [""] * N
        for k, list_of_char in groups_char.items():
            list_of_char.sort()
            list_of_indices = groups_i[k]
            for idx, value in zip(list_of_indices, list_of_char):
                res[idx] = value

        return "".join(res)


def main():
    sol = Solution()
    res = sol.smallestStringWithSwaps("qdwyt", [[2, 3], [3, 2], [0, 1], [4, 0], [3, 2]])


if __name__ == "__main__":
    main()
