class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        n = len(nums)
        left_idx = bisect_left(nums, target)
        right_idx = bisect_left(nums, target + 1) - 1
        if left_idx >= n or nums[left_idx] != target:
            left_idx = -1
        if right_idx >= n or nums[right_idx] != target:
            right_idx = -1
        return [left_idx, right_idx]
