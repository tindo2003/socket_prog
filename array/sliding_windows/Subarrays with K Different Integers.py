from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # following Striver approach. find sliding window containing <= k distinct integers. AND find sliding window containing <= k-1 distinct integers.
        def sliding_window(boundary):
            my_dict = defaultdict(int)
            n = len(nums)
            cnt = 0
            l = 0
            for r in range(n):
                my_dict[nums[r]] += 1
                while len(my_dict) > boundary:
                    my_dict[nums[l]] -= 1
                    if my_dict[nums[l]] == 0:
                        del my_dict[nums[l]]
                    l += 1

                cnt += r - l + 1
            return cnt

        ltqd_to_k = sliding_window(k)
        # find number <= k
        # find number <= k-1
        ltqd_to_k_minus_1 = sliding_window(k - 1)

        return ltqd_to_k - ltqd_to_k_minus_1
