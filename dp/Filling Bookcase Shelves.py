from typing import List
from math import inf
from collections import defaultdict


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        N = len(books)
        cache = defaultdict(int)

        def dfs(idx):
            if idx >= N:
                return 0
            if idx in cache:
                return cache[idx]
            max_height = -inf
            res = inf
            remaining_thickness = shelfWidth
            for new_idx in range(idx + 1, N + 1):
                thickness, height = books[new_idx - 1]
                max_height = max(max_height, height)
                remaining_thickness -= thickness
                if remaining_thickness < 0:
                    break
                res = min(res, max_height + dfs(new_idx))
            cache[idx] = res
            return res

        return dfs(0)


def main():
    sol = Solution()
    res = sol.minHeightShelves(
        [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4
    )
    print(res)


if __name__ == "__main__":
    main()
