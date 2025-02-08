class Solution:
    def binaryGap(self, n: int) -> int:
        # store the indices where the bit is 1
        A = [i for i in range(32) if (n >> i) & 1]
        res = 0
        for i in range(len(A) - 1):
            res = max(res, A[i + 1] - A[i])
        return res
