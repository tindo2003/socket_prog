from math import inf


class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s)
        pref_cnt_zero = [0] * N
        suffix_cnt_one = [0] * N
        zero_cnt = one_cnt = 0
        for i in range(N):
            if s[i] == "0":
                zero_cnt += 1
            pref_cnt_zero[i] = zero_cnt
        for i in range(N - 1, -1, -1):
            if s[i] == "1":
                one_cnt += 1
            suffix_cnt_one[i] = one_cnt

        maxi = -inf
        for i in range(1, N):
            left = right = 0
            if i - 1 >= 0:
                left = pref_cnt_zero[i - 1]
            right = suffix_cnt_one[i]
            maxi = max(maxi, left + right)
        return maxi
