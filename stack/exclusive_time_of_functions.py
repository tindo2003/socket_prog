from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # the idea is to update the exclusive time whenever there are new events. the start of an event could mean the previous event has been running for x time since started. 
        stack = []
        latest_time = 0
        res = [0] * n
        for log in logs:
            id, kw, time_val = log.split(":")
            id = int(id)
            time_val = int(time_val)
            if kw == "end":
                time_val += 1
            if kw == "start":
                if stack:
                    top_id = stack[-1]
                    res[top_id] += time_val - latest_time
                stack.append(id)
            else:
                stack.pop()
                res[id] += time_val - latest_time
            latest_time = time_val
        return res
