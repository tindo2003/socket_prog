from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(prices)
        for i in range(len(prices) - 1, -1, -1):
            cur_price = prices[i]
            while stack:
                top = stack[-1]
                if prices[top] > cur_price:
                    stack.pop()
                else:
                    break
            if stack:
                res[i] = stack[-1]
            stack.append(i)

        f = prices.copy()
        for i in range(len(f)):
            if res[i] != -1:
                f[i] = prices[i] - prices[res[i]]

        return f
