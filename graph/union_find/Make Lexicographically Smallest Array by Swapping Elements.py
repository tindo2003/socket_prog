class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # This solution uses a greedy approach combined with Union-Find (Disjoint Set Union).
        # Elements within a connected component (where differences between adjacent elements are <= limit)
        # can be rearranged freely to achieve the lexicographically smallest array.
        # Union-Find helps group elements into components based on the limit constraint.
        # 2 ptr helps speed this up
        nums.append(inf)
        nums = list(enumerate(nums))
        nums.sort(key=lambda x: x[1])
        l = 0
        n = len(nums)
        res = [0] * n
        for r in range(1, n):
            cur_ele = nums[r][1]
            prev_ele = nums[r - 1][1]
            if cur_ele - prev_ele > limit:
                mini_arr = nums[l:r]
                mini_arr.sort(key=lambda x: x[0])
                for i, ele in enumerate(mini_arr):
                    res[ele[0]] = nums[l + i][1]
                l = r
        return res[0 : n - 1]
