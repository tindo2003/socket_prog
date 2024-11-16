from typing import List
from math import inf


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        def bin_search(tgt, arr):
            res = -1
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                cur_ele = arr[mid][0]
                if cur_ele <= tgt:
                    res = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return res

        items.sort(key=lambda x: x[0])
        maxi = -inf
        for idx in range(len(items)):
            price, beauty = items[idx]
            if beauty > maxi:
                maxi = beauty
            items[idx][1] = maxi

        res = []
        for query in queries:
            idx = bin_search(query, items)
            if idx != -1:
                res.append(items[idx][1])

        return res


if __name__ == "__main__":
    sol = Solution()
    sol.maximumBeauty([[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6])
