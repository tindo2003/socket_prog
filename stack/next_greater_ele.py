
from typing import List 

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_dict = {}
        stack = []
        n = len(nums2)

        for idx in range(n-1, -1, -1):
            cur_ele = nums2[idx]
        
            while stack:
                top = stack[-1]
                if cur_ele > nums2[top]:
                    stack.pop()
                else:
                    break 

            if not stack:
                my_dict[cur_ele] = -1
            else:
                my_dict[cur_ele] = stack[-1]
            stack.append(idx)
     
        tmp = [nums2[my_dict[num]] if my_dict[num] != -1 else -1 for num in nums1]
        return tmp

def main():
    sol = Solution()
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    res = sol.nextGreaterElement(nums1, nums2)
    print(res)

if __name__ == "__main__":
    main()