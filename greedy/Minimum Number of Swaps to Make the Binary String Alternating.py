from math import inf


class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        expect_s1, expect_s2 = "", ""
        if n % 2 == 0:
            expect_s1 = "01" * (n // 2)
        else:
            expect_s1 = "01" * (n // 2) + "0"

        if n % 2 == 0:
            expect_s2 = "10" * (n // 2)
        else:
            expect_s2 = "10" * (n // 2) + "1"

        res = inf
        cnt1, cnt0 = 0, 0
        for c1, c2 in zip(s, expect_s1):
            if c1 != c2:
                if c2 == "0":
                    cnt0 += 1
                else:
                    cnt1 += 1
        if cnt1 == cnt0:
            res = cnt1

        cnt1, cnt0 = 0, 0
        for c1, c2 in zip(s, expect_s2):
            if c1 != c2:
                if c2 == "0":
                    cnt0 += 1
                else:
                    cnt1 += 1
        if cnt1 == cnt0:
            res = min(res, cnt1)
        if res == inf:
            return -1
        return res
