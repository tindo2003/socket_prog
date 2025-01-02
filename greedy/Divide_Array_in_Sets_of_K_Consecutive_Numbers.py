from typing import List
from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        nums.sort()
        freq = Counter(nums)
        for num in nums:
            # if num hasn't been used already
            if freq[num] > 0:
                range_from_num = [item for item in range(num, num + k)]
                for i in range_from_num:
                    if freq[i] > 0:
                        freq[i] -= 1
                    else:
                        return False
        return True
