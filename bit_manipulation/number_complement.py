class Solution:
    def findComplement(self, num: int) -> int:
        res = []
        while num:
            digit = num % 2
            if digit == 0:
                res.append(1)
            else:
                res.append(0)
        res.reverse()
        return int(res, 2)