from typing import List 
from bisect import bisect_left as lower_bound

def find_pairs(nums: List[int]):
    nums.sort()
    ans = 0 
    N = len(nums)
    print(nums)
    for idx in range(N):
        cur_num = nums[idx]
        if cur_num < 0: continue # this is quite important.
        # everything to the left of j is less than -cum_num + 1; everything to the right of j is greater than 
        # -cur_sum + 1
        j = lower_bound(nums, -cur_num + 1) 
        print(idx, j)
        ans += idx - j
    return ans 

def main():
    nums = [-4, 4, -5, 5, 3, -2, -3, -1, 2, 1]
    ans = find_pairs(nums)
    print(ans)

if __name__ == "__main__":
    main()
