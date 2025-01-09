from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        m_sum = sum(rolls)
        n_m_sum = mean * (n + m)
        n_sum = n_m_sum - m_sum

        if n_sum < n or n_sum > 6 * n:
            return []
        res = []
        for i in range(n):
            remaining_slots = n - 1 - i
            amnt_add = min(6, n_sum - remaining_slots)
            n_sum -= amnt_add
            res.append(amnt_add)

        return res


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        nplusm = m + n
        s = nplusm * mean
        other_s = sum(rolls)
        wanted_s = s - other_s
        if wanted_s < 0:

            return []
        whole, remainder = divmod(wanted_s, n)

        if not (0 < whole <= 6):
            return []
        res = []
        # greedy: try the biggest possible numbers first
        while remainder > 0:
            highest = min(6, whole + remainder)
            d = highest - whole
            if d == 0:
                return []
            tmp = remainder // d
            remainder -= tmp * d
            res += [highest] * tmp
            n -= tmp
        res += [whole] * n
        return res
