from typing import List
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        my_dict = defaultdict(list)
        for idx, val in enumerate(s):
            my_dict[val].append(idx)

        def binary_search(tgt, lst):
            # return index in the list not the actual value
            # https://www.youtube.com/watch?v=Csqlac6k1U4&ab_channel=CodewithAlisha
            l = 0
            r = len(lst) - 1
            res = -1
            while l <= r:
                m = (l + r) // 2
                if lst[m] > tgt:
                    res = m
                    r = m - 1
                else:
                    l = m + 1
            return res

        def is_subq(word):
            maxi = -1
            for c in word:
                # find index greater than or equal to the previous index
                tmp = binary_search(maxi, my_dict[c])
                if tmp == -1:
                    return False
                # maxi is guaranteed to be increasing thanks to binary search
                maxi = my_dict[c][tmp]
            return True

        cnt = 0
        for word in words:
            if is_subq(word):
                cnt += 1
        return cnt
