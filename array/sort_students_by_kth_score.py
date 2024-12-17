from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        N, M = len(score), len(score[0])
        lst = []
        for r in range(N):
            val = score[r][k]
            lst.append((val, r))
        lst.sort(key=lambda x: x[0], reverse=True)
        # print(lst)
        res = []
        for val, idx in lst:
            res.append(score[idx])
        return res
