class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        my_dict = {}
        for num in nums:
            idx = 0
            while num > 0:
                num, remain = divmod(num, 10)
                if idx not in my_dict:
                    my_dict[idx] = [0] * 10
                my_dict[idx][remain] += 1
                idx += 1

        res = 0
        N = len(nums)
        for arr in my_dict.values():
            for cnt in arr:
                res += (cnt * (N - cnt))
        return res // 2 # the main trick of this problem