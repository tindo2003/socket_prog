from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def recur(idx):
            if idx == n:
                res.append(nums.copy())
                return
            seen = set()
            for idx_to_swap in range(idx, n):
                if nums[idx_to_swap] in seen:
                    continue
                seen.add(nums[idx_to_swap])
                # swap elements at idx and new_idx
                nums[idx], nums[idx_to_swap] = nums[idx_to_swap], nums[idx]
                recur(idx + 1)
                nums[idx], nums[idx_to_swap] = nums[idx_to_swap], nums[idx]

        recur(0)
        return res
