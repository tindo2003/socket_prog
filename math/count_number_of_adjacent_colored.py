class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        n = n - 1
        d = 4
        a = 4
        s = (n / 2) * (2 * a + (n - 1) * d)
        return int(s) + 1
