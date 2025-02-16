from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def recur(idx):
            if idx == n:
                res.append(nums.copy())
                return
            for new_idx in range(idx, n):
                # swap elements at idx and new_idx
                nums[idx], nums[new_idx] = nums[new_idx], nums[idx]
                recur(idx + 1)
                nums[idx], nums[new_idx] = nums[new_idx], nums[idx]
                
        recur(0)
        return res


def main():
    sol = Solution()
    nums = [1, 2, 3]
    res = sol.permute(nums)
    print(res)


if __name__ == "__main__":
    main()
