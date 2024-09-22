from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        def binary_search(l, target):
            r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target: return True 
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        nums.sort()
        ans = set()
        for idx, num in enumerate(nums):
            wanted_num = num + k 
            find = binary_search(idx + 1, wanted_num)
            if find: ans.add((num, wanted_num))
        return len(ans)      