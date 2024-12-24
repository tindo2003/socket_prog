from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        N = len(chars)
        res = []
        l = 1
        l_ptr = 0
        for idx in range(N - 1):
            val = chars[idx]
            if val != chars[idx + 1]:
                chars[l_ptr] = val
                l_ptr += 1
                if l > 1:
                    str_l = str(l)
                    for i in range(len(str_l)):
                        chars[l_ptr] = str_l[i]
                        l_ptr += 1
                l = 1
            else:
                l += 1
        chars[l_ptr] = val = chars[-1]
        l_ptr += 1
        if l != 1:
            str_l = str(l)
            for i in range(len(str_l)):
                chars[l_ptr] = str_l[i]
                l_ptr += 1

        return l_ptr
