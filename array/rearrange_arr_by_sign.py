from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        neg_num, pos_num = [], []
        for num in nums:
            if num < 0:
                neg_num.append(num)
            else:
                pos_num.append(num)
        res = []
        idx = 0
        for i in range(N//2):
            res.append(pos_num[i])
            res.append(neg_num[i])
        return res