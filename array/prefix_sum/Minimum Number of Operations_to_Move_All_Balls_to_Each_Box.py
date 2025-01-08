from typing import List
from itertools import accumulate
from collections import deque


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        box_lst = list(map(int, list(boxes)))
        N = len(box_lst)
        left_s = list(accumulate(box_lst, initial=0))[1:]
        cur = 0
        right_s = deque([])
        for idx in range(N - 1, -1, -1):
            cur += box_lst[idx]
            right_s.appendleft(cur)
        right_s = list(right_s)
        res = []
        for idx, item in enumerate(box_lst):
            cnt = 0
            for i in range(0, idx):
                cnt += left_s[i]
            for i in range(N - 1, idx, -1):
                cnt += right_s[i]
            res.append(cnt)
        return res
