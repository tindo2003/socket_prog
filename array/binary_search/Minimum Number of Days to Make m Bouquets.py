class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if (len(bloomDay) // m) < k:
            return -1

        def is_possible(bloom_day):
            res = 0
            cnt = 0
            for d in bloomDay:
                if d <= bloom_day:
                    cnt += 1
                else:
                    res += cnt // k
                    cnt = 0
            res += cnt // k
            return res >= m

        l, r = min(bloomDay), max(bloomDay)
        res = -1
        while l <= r:
            bloom_day = (l + r) // 2
            if is_possible(bloom_day):
                r = bloom_day - 1
                res = bloom_day
            else:
                l = bloom_day + 1
        return res
