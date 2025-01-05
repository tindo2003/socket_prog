from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # VERY SIMILAR TO RANGE ADDITION
        N = len(s)
        s_lst = [0] * N
        for start, end, change in shifts:
            if change == 0:
                d = -1
            else:
                d = 1
            s_lst[start] = s_lst[start] + d
            if end + 1 < N:
                s_lst[end + 1] = s_lst[end + 1] - d

        for idx in range(1, N):
            s_lst[idx] += s_lst[idx - 1]

        my_lst = list(s)
        for idx, char in enumerate(my_lst):
            tmp = ord(char) - 97
            tmp = (tmp + s_lst[idx]) % 26
            my_lst[idx] = chr(tmp + 97)
        return "".join(my_lst)
