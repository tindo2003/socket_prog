from typing import List
from collections import Counter


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            freq = Counter(s)
            sorted_freq = sorted(freq.items(), key=lambda x: x[0])
            return sorted_freq[0][1]

        for idx, word in enumerate(words):
            words[idx] = f(word)
        words.sort()

        def bin_search(tgt):
            l, r = 0, len(words) - 1
            res = -1
            while l <= r:
                m = (l + r) // 2
                if tgt < words[m]:
                    r = m - 1
                    res = m
                else:
                    l = m + 1
            return res

        for idx, q in enumerate(queries):
            tgt = f(q)
            tmp = bin_search(tgt)
            if tmp == -1:
                queries[idx] = 0
            else:
                queries[idx] = len(words) - tmp
        return queries
