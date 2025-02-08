class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        my_dict = {start: idx for idx, (start, end) in enumerate(intervals)}
        new_arr = sorted(intervals, key=lambda x: x[0])
        new_arr = [start for start, end in new_arr]

        res = []
        for itv in intervals:
            tgt = itv[1]
            idx = bisect_left(new_arr, tgt)
            if idx >= len(intervals):
                res.append(-1)
            else:
                my_start = new_arr[idx]
                res.append(my_dict[my_start])
        return res
