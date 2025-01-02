from typing import List
from collections import defaultdict


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        def bin_search(tgt):
            """
            find idx of element >= tgt
            """
            res = -1
            l, r = 0, len(days) - 1
            while l <= r:
                middle = (l + r) // 2
                if tgt <= days[middle]:
                    res = middle
                    r = middle - 1
                else:
                    l = middle + 1
            if res == -1:
                return None
            return days[res]

        memo = defaultdict(int)

        def dfs(cur_day):
            # option1
            option1 = costs[0]
            option2 = costs[1]
            option3 = costs[2]
            if cur_day > 365:
                return 0
            if cur_day in memo:
                return memo[cur_day]
            nxt_day = bin_search(cur_day + 1)
            if nxt_day:
                option1 += dfs(nxt_day)
            nxt_day = bin_search(cur_day + 7)
            if nxt_day:
                option2 += dfs(nxt_day)
            nxt_day = bin_search(cur_day + 30)
            if nxt_day:
                option3 += dfs(nxt_day)
            min_cost = min(option1, option2, option3)
            memo[cur_day] = min_cost
            return min_cost

        return dfs(days[0])


def main():
    sol = Solution()
    res = sol.mincostTickets(
        days=[1, 2, 3, 4, 6, 8, 9, 10, 13, 14, 16, 17, 19, 21, 24, 26, 27, 28, 29],
        costs=[3, 14, 50],
    )


if __name__ == "__main__":
    main()
