
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        two_idx, three_idx, five_idx = 0, 0, 0
        while n > 1:
            next_num = min(2*dp[two_idx], 3*dp[three_idx], 5*dp[five_idx])
            if next_num == 2*dp[two_idx]: two_idx += 1 
            if next_num == 3*dp[three_idx]: three_idx += 1 
            if next_num == 5*dp[five_idx]: five_idx += 1 
            dp.append(next_num)
            n -= 1

        return dp[-1]