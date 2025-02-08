class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # [[5,10],[6,8],[1,5],[2,3],[1,10]]
        #
        h = []
        for left, right in intervals:
            heappush(h, (left, 0))
            heappush(h, (right, 1))

        num_overlapping = 0
        res = 0
        while h:
            num, status = heappop(h)
            if status == 0:
                num_overlapping += 1
                res = max(res, num_overlapping)
            else:
                num_overlapping -= 1
        return res
