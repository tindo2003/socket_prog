from heapq import heappush, heappop
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # sort based on enq time
        idx_tasks = list(enumerate(tasks))
        idx_tasks.sort(key=lambda x: x[1][0])
        time = idx_tasks[0][1][0]
        idx = 0
        n = len(tasks)
        h = []
        res = []
        while idx < n:
            while idx < n and idx_tasks[idx][1][0] <= time:
                heappush(h, (idx_tasks[idx][1][1], idx_tasks[idx][0]))
                idx += 1
            if h:
                processing_time, i = heappop(h)
            else:
                time = idx_tasks[idx][1][0]
                continue
            res.append(i)
            time += processing_time
        while h:
            processing_time, i = heappop(h)
            res.append(i)
        return res
