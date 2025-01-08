from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7

        def arithmetic_sum(lower, upper, n):
            return (n * (upper + lower)) // 2

        inventory.sort(reverse=True)
        N = len(inventory)
        idx = 0
        factor = 1
        res = 0
        while True:
            cur_val = inventory[idx]
            if idx + 1 >= N:
                break
            next_max = inventory[idx + 1]
            lower_bound = next_max + 1
            upper_bound = cur_val
            n = upper_bound - lower_bound + 1
            amnt_to_subtract = n * factor
            if amnt_to_subtract > orders:
                break

            profit = arithmetic_sum(lower_bound, upper_bound, n) * factor
            res += profit
            idx += 1
            factor += 1
            orders -= amnt_to_subtract

        whole, remainder = divmod(orders, factor)
        lower_bound = cur_val - whole + 1
        upper_bound = cur_val
        n = whole
        profit = arithmetic_sum(lower_bound, upper_bound, n) * factor
        #########
        remaining_profit = (cur_val - whole) * remainder
        res += profit
        res += remaining_profit
        orders = 0
        return res % MOD
