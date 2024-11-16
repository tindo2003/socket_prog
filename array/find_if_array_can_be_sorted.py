from typing import List 
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def find_number_of_ones(num):
            binary_res = bin(num)[2:]
            return binary_res.count('1')
        new = sorted(nums)
        if new == nums: return True
        seen = set([nums[0]])
        prev = [0] * len(nums)
        prev[0] = find_number_of_ones(nums[0])
        max_range = min_range = prev_max = nums[0]
        first_change = True
        for idx in range(1, len(nums)):
            num = nums[idx]
            tmp = find_number_of_ones(num)
            if tmp != prev[idx - 1]:
                if not first_change:
                    if min_range < prev_max: 
                        return False
                first_change = False
                if tmp in seen: 
                    return False
                else:
                    seen.add(tmp)
                    prev_max = max_range
                    max_range = num
                    min_range = num
            max_range = max(max_range, num)
            min_range = min(min_range, num)
            prev[idx] = tmp
        if not first_change and min_range < prev_max: 
            return False
        return True