from collections import defaultdict


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # TIP: recursion on the current length of the string
        # WILL MLE but mainly cuz recursion
        memo = defaultdict(int)

        def dfs(cur_len):
            if cur_len > high:
                return 0
            if cur_len in memo:
                return memo[len(cur_len)]
            left = dfs(cur_len + zero)
            right = dfs(cur_len + one)
            total = 0
            if low <= cur_len <= high:
                total = left + right + 1
            else:
                total = left + right
            memo[cur_len] = total
            return total

        return dfs("")


# OR #
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # TIP: recursion on the current length of the string
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        for cur_len in range(high, -1, -1):
            use_zero = use_one = 0
            if cur_len + zero <= high:
                use_zero = dp[cur_len + zero]
            if cur_len + one <= high:
                use_one = dp[cur_len + one]
            dp[cur_len] += use_zero + use_one
            if low <= cur_len <= high:
                dp[cur_len] += 1
        return dp[0] % MOD


def main():
    sol = Solution()
    res = sol.countGoodStrings(1, 1, 1, 1)
    print(res)


if __name__ == "__main__":
    main()
