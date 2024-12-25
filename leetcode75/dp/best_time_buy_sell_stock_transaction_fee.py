from enum import Enum
from typing import List
from collections import defaultdict


from enum import Enum
from typing import List
from collections import defaultdict


class Action(Enum):
    HOLDING = 1
    EMPTY = 0


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = defaultdict(int)
        HOLDING, EMPTY = Action.HOLDING, Action.EMPTY  # Aliases for brevity

        def dfs(idx: int, my_bool: bool) -> int:
            if idx == len(prices):
                return 0
            if (idx, my_bool) in memo:
                return memo[(idx, my_bool)]
            do_smth = not_do = 0
            if my_bool == HOLDING:
                # not sell
                not_do = dfs(idx + 1, HOLDING)
                # sell
                do_smth = prices[idx] - fee + dfs(idx + 1, EMPTY)
            else:
                # buy at current index
                do_smth = -prices[idx] + dfs(idx + 1, HOLDING)
                # skip this deal
                not_do = dfs(idx + 1, EMPTY)
            res = max(do_smth, not_do)
            memo[(idx, my_bool)] = res
            return res

        return dfs(0, EMPTY)
