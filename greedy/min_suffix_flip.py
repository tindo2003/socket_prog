class Solution:
    def minFlips(self, target: str) -> int:
        prev = "0"
        res = 0 
        for num in target:
            if num != prev:
                res += 1
                prev = num
        return res