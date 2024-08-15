from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # subsequences = not necessarily contiguous
        res = set()
        def helper(cur_idx: int, cur_lst: List[int]):
            if cur_idx >= len(nums):
                if len(cur_lst) >= 2: 
                    res.add(tuple(cur_lst))
                return 

            cur_ele = nums[cur_idx] 
            if (cur_lst and cur_lst[-1] <= cur_ele) or not cur_lst:
                cur_lst.append(cur_ele)
                # pick 
                helper(cur_idx + 1, cur_lst)
                cur_lst.pop()
            # not pick
            helper(cur_idx + 1, cur_lst)
            
                    
        helper(0, [])
        return [list(seq) for seq in res] 


def main():
    sol = Solution()
    nums = [1, 1, 2, 2, 3, 2, 3, 4]
    res = sol.findSubsequences(nums)
    print(res)

if __name__ == "__main__":
    main()
