class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # (1xor3)xor(1xor4)xor(2xor3)xor(2xor4)
        # even xor of itself is 0
        # odd xor of itself is itself
        n, m = len(nums1), len(nums2)
        if m % 2 == 0:
            nums1 = [0] * n
        if n % 2 == 0:
            nums2 = [0] * m
        res = 0
        for i in range(n):
            res ^= nums1[i]
        for i in range(m):
            res ^= nums2[i]
        return res
