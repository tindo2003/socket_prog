from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        my_set = set()
        sorted_freq = sorted(freq.items(), key=lambda x: x[1])
        cnt = 0
        for k, v in sorted_freq:
            while v in my_set:
                v -= 1
                cnt += 1
            # if it does not appear, do not count
            if v > 0:
                my_set.add(v)
        return cnt
