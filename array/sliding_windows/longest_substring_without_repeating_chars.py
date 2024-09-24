
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        my_dict = {}
        N = len(s)
        res = 0
        for r in range(N):
            cur_ele = s[r]
            while l < N and cur_ele in my_dict:
                del my_dict[s[l]]
                l += 1
            my_dict[cur_ele] = 1
            res = max(res, r - l + 1)
        return res