class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0
        # objective: find the prefix
        for bit in range(31, -1, -1):
            left_bit = left & (1 << bit)
            right_bit = right & (1 << bit)
            if left_bit != right_bit:
                break
            else:
                res |= left_bit & (1 << bit)
        return res
