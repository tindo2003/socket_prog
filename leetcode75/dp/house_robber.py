from typing import List
from collections import defaultdict


class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        memo = defaultdict(int)

        def dfs(idx: int, picked: bool):
            picked_val = 0
            nonpicked_val = 0
            if idx == N:
                return 0
            if (idx, picked) in memo:
                return memo[(idx, picked)]
            if not picked:
                nonpicked_val = dfs(idx + 1, False)
                picked_val = nums[idx] + dfs(idx + 1, True)
            else:
                nonpicked_val = dfs(idx + 1, False)
            tmp = max(picked_val, nonpicked_val)
            memo[(idx, picked)] = tmp
            return tmp

        return dfs(0, False)


def main():
    sol = Solution()
    res = sol.rob([2, 1, 2])
    print(res)


if __name__ == "__main__":
    main()
