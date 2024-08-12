from typing import List 

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    nums.sort()
    for i in range(1, len(nums), 3):
      if nums[i] != nums[i-1]:
        return i-1
    return nums[len(nums) - 1]
        
        
               
               

def main():
    sol = Solution()
    nums = [0,1,0,1,0,1,99]
    res = sol.singleNumber(nums)
    print(res)
if __name__ == "__main__":
  main()