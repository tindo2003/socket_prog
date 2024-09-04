from typing import List 
from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cur_sum = 0 
        my_dict = defaultdict(int)
        for num in nums:
            cur_sum += num
            mod = cur_sum % k 
            if cur_sum % k == 0 or mod in my_dict:
                return True 
            my_dict[mod] = 1
        return False 

def main():
    sol = Solution()
    nums = [23,2,4,6,6]
    k = 7
    res = sol.checkSubarraySum(nums, k)
    print(res)

if __name__ == "__main__":
    main()