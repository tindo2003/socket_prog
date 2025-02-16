from typing import List
from collections import defaultdict, Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        my_dict = defaultdict(int)
        # THE TRICK: keep the maximum of each characters across all words in words2
        for idx, word in enumerate(words2):
            freq = Counter(word)
            for k, v in freq.items():
                my_dict[k] = max(v, my_dict[k])

        res = []
        for word in words1:
            freq = Counter(word)
            good = True
            for k, v in my_dict.items():
                if v > freq[k]:
                    good = False
                    break
            if good:
                res.append(word)
        return res
