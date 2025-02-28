from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        decreasing = [0] * n
        decreasing[-1] = 1
        for i in range(n - 2, -1, -1):
            if security[i] >= security[i + 1]:
                decreasing[i] = decreasing[i + 1] + 1
            else:
                decreasing[i] = 1

        increasing = [0] * n
        increasing[0] = 1
        for i in range(1, n):
            if security[i] >= security[i - 1]:
                increasing[i] = increasing[i - 1] + 1
            else:
                increasing[i] = 1

        res = []
        for i in range(n):
            if i - time >= 0 and i + time < n:
                if (decreasing[i - time] - decreasing[i]) >= time and (
                    increasing[i + time] - increasing[i]
                ) >= time:
                    res.append(i)
        return res
