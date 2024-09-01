from typing import List 
import heapq 
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        h = []
        if not tasks: return []
        res = []
        indexed = list(enumerate(tasks))
        # Sort based on the value
        sorted_indexed = sorted(indexed, key=lambda x: x[1])
        heapq.heappush(h, (sorted_indexed[0][1][1], sorted_indexed[0][0]))
        time = sorted_indexed[0][1][0]
        idx = 1 
        N = len(tasks)
        while h:
            process_time, idx1 = heapq.heappop(h)
            res.append(idx1)
            time += process_time
            while idx < N and sorted_indexed[idx][1][0] <= time:
                heapq.heappush(h, (sorted_indexed[idx][1][1], sorted_indexed[idx][0]))
                idx += 1
            # if the start time is greater than the end time of the currently processed task
            if not h and idx < N:
                time = sorted_indexed[idx][1][0]
                while idx < N and sorted_indexed[idx][1][0] <= time:
                    heapq.heappush(h, (sorted_indexed[idx][1][1], sorted_indexed[idx][0]))
                    idx += 1
        return res