class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = 0 
        res = 1
        N = len(nums)
        for r in range(1, N):
            if nums[r] <= nums[r-1]:
                l = r
            else:
                res = max(res, r - l + 1)
        return res