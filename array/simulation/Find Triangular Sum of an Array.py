from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        tmp_lst = nums.copy()
        length = len(nums)
        while length != 1:
            for idx in range(length - 1):
                tmp_lst[idx] = (nums[idx] + nums[idx + 1]) % 10

            nums = tmp_lst
            length -= 1
        return tmp_lst[0]
