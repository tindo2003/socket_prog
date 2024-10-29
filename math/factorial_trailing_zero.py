class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        cur_division = 1
        while n // cur_division != 0:
            cur_division *= 5
            res += n // cur_division
        return res
