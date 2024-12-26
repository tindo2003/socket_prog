from collections import defaultdict


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # The problem is similar to "Target Sum" problem.
        # Each face of the die represents a possible choice (similar to the choice of operations).
        # The number of dice corresponds to the "length of the array".

        MOD = 10**9 + 7
        memo = defaultdict(int)

        def dfs(idx: int, cur_sum: int):
            # Base case: If we've used all dice, check if we've reached the target sum
            if idx == n:
                return 1 if cur_sum == target else 0

            if cur_sum >= target:
                return 0

            if (idx, cur_sum) in memo:
                return memo[(idx, cur_sum)]

            # Recursive step: Try all possible outcomes for the current die
            total = 0
            for i in range(1, k + 1):
                total += dfs(idx + 1, cur_sum + i)

            memo[(idx, cur_sum)] = total
            return total

        return dfs(0, 0) % MOD
