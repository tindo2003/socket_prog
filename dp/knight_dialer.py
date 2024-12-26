import copy


class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 10

        memo = [2, 2, 2, 2, 3, 0, 3, 2, 2, 2]
        m = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }
        if n == 2:
            return sum(memo)
        for _ in range(3, n + 1):
            deep_copied = copy.deepcopy(memo)
            for idx in range(10):
                s = 0
                for neighbor in m[idx]:
                    s += deep_copied[neighbor]
                memo[idx] = s
        return sum(memo) % MOD
