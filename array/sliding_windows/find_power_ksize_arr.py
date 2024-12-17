from typing import List 

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        N = len(nums)
        maxi = nums[0]
        res = [-1] * (N - k + 1)
        prev_correct = True
        for i in range(1, k):
            if nums[i] - nums[i - 1] != 1:
                prev_correct = False
            maxi = max(nums[i], maxi)
        if prev_correct:
            res[0] = maxi
        else:
            res[0] = -1

        l = 0
        for r in range(k, N):
            l += 1
            cur = nums[r]

            if prev_correct:
                maxi = max(maxi, cur)
                if cur - nums[r - 1] == 1:
                    res[r - k + 1] = maxi
                else:
                    prev_correct = False
            else:
                maxi = nums[l]
                prev_correct = True
                for i in range(l + 1, r + 1):
                    maxi = max(maxi, nums[i])
                    if nums[i] - nums[i - 1] != 1:
                        prev_correct = False
                if prev_correct:
                    res[r - k + 1] = maxi

        return res
