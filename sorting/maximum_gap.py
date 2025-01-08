from typing import List
import math


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        mini, maxi = min(nums), max(nums)
        max_diff = maxi - mini
        n = len(nums)
        # number of bucket is n+1
        res = 0
        # if avg_gap = 5, then the buckets might cover ranges like: [ min , min + 5 ) , [ min + 5 , min + 10 ), ...Notice the end is exclusive
        buckets = [[] for _ in range(n + 1)]
        bucket_size = math.ceil(max_diff / (n - 1))
        if bucket_size == 0:
            return 0
        for num in nums:
            bucket_idx = (num - mini) // bucket_size
            buckets[bucket_idx].append(num)

        res = 0
        prev_max = max(buckets[0])
        for i in range(1, n + 1):
            # skip empty buckets
            if len(buckets[i]) > 0:
                cur_min = min(buckets[i])
                res = max(res, cur_min - prev_max)
                prev_max = max(buckets[i])
        return res
