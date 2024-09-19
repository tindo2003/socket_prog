class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        is_neg = False
        if x < 0:
            x *= - 1
            is_neg = True
        while x > 0:
            digit = x % 10
            x = x // 10
            res = res * 10 + digit 
        if is_neg: return res * -1 
        return res