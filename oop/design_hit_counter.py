class HitCounter:

    def __init__(self):
        """
        @param timestamp: the timestamp
        @return: nothing
        """
        pass
        self.times = []
    def hit(self, timestamp: int):
        """
        @param timestamp: the timestamp
        @return: the count of hits in recent 300 seconds
        """
        self.times.append(timestamp)

    def get_hits(self, timestamp: int) -> int:
        prev_time = timestamp - 300 + 1
        if prev_time < 0:
            prev_time = 0

        l = 0 
        r = len(self.times) - 1
        right_idx = -1
        while l <= r:
            mid = (l + r) // 2
            cur_ele = self.times[mid]
            if cur_ele > timestamp:
                r = mid - 1
            else:
                l = mid + 1
                if cur_ele >= prev_time:
                    right_idx = mid

        l = 0 
        r = len(self.times) - 1
        left_idx = -1
        while l <= r:
            mid = (l + r) // 2
            cur_ele = self.times[mid]
            if cur_ele == prev_time:
                left_idx = mid 
                break
            if cur_ele > prev_time:
                r = mid - 1
                if cur_ele < timestamp:
                    left_idx = mid
            else:
                l = mid + 1

        if right_idx == -1 and left_idx == -1: return 0
        return right_idx - left_idx + 1

