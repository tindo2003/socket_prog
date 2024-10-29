from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = inf
        changed = False
        while l <= r:
            mid = (l + r) // 2
            cur_num = nums[mid]
            res = min(res, cur_num)
            if cur_num < nums[l]:  # not sorted
                r = mid - 1
            else:  # sorted
                res = min(
                    res, nums[l]
                )  # since we know it is sorted, we just take the min with the most left element and move to the right to check
                l = mid + 1
        return res
