import math 
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # a^2 + b^2 = c
        # when b = 0, a^2 = c -> a = sqrt(c)
        if c == 0: return True
        for a in range(math.ceil(math.sqrt(c))):
            b = math.sqrt(c - a**2)
            if a**2 + int(b)**2 == c:
                return True
        return False