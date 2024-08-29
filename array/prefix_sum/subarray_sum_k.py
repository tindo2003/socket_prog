from typing import List
from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # nums = [1,2,3,5], k = 5
        # 0 + ...+ i-1 + i + ..  + j  = f(j)
        # 0 + ... + i-1 = f(i-1)
        # i + ... + j = k 
        # f(j) = f(i-1) + k 
        # f(j) - k = f(i-1)
        counter = Counter()
        current = 0
        counter[current] = 1
        ans = 0
        for num in nums:
            current += num 
            prev = current - k 
            ans += counter[prev]
            counter[current] += 1
        return ans 
            