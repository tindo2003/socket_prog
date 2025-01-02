from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        N = len(words)
        prefix_sum = [0] * N
        vowels = "ueoai"
        cur_sum = 0
        for idx, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                cur_sum += 1
            prefix_sum[idx] = cur_sum
        res = []
        for start, end in queries:
            tmp = prefix_sum[end]
            if start - 1 >= 0:
                tmp -= prefix_sum[start - 1]
            res.append(tmp)
        return res
