from collections import defaultdict


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # best video
        res = 1
        my_dict = defaultdict(int)
        N = len(s)
        my_dict[s[0]] = 1
        for i in range(1, N):
            cur_char = s[i]
            max_val = 1
            for offset in range(-k, k + 1):
                new_val = ord(cur_char) + offset
                if ord("a") <= new_val <= ord("z"):
                    new_char = chr(new_val)
                    if new_char in my_dict:
                        max_val = max(max_val, my_dict[new_char] + 1)
            my_dict[cur_char] = max_val
            res = max(res, max_val)
        return res
