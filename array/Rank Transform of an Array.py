from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        N = len(arr)
        res = [0] * N
        rank = 1
        new_arr = sorted(list(enumerate(arr)), key=lambda x: x[1])
        for i, (idx, val) in enumerate(new_arr):
            if i == 0:
                res[idx] = rank
            else:
                _, val1 = new_arr[i - 1]
                if val == val1:
                    res[idx] = rank
                    continue
                else:
                    rank += 1
                    res[idx] = rank
        return res
