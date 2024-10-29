from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        counter = Counter(s)
        odd_cnt = 0
        for ke, freq in counter.items():
            if freq % 2 == 1:
                odd_cnt += 1
        if odd_cnt > k:
            return False
        return True
