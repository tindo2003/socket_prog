from typing import (
    List,
)


class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """

    def get_modified_array(self, length: int, updates: List[List[int]]) -> List[int]:
        # Write your code here
        nums = [0] * length
        N = len(nums)
        for start, end, change in updates:
            nums[start] += change
            if end + 1 < N:
                nums[end + 1] -= change
        for idx in range(1, N):
            nums[idx] += nums[idx - 1]
        return nums
