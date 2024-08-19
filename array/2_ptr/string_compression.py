from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt = 1
        N = len(chars)
        l = 0
        res = 0
        prev = chars[0]
        for idx in range(1, N):
            if chars[idx] != chars[idx - 1]:
                chars[l] = prev 
                prev = chars[idx]
                if cnt > 1:
                    cnt_str = str(cnt)
                    tmp = 0
                    while tmp < len(cnt_str):
                        l += 1
                        chars[l] = cnt_str[tmp]
                        tmp += 1
                    res += (len(str(cnt)) + 1)
                else:
                    res += 1
                l += 1
                cnt = 1
            else:
                cnt += 1

        chars[l] = prev
        if cnt > 1:
            cnt_str = str(cnt)
            tmp = 0   
            while tmp < len(cnt_str):
                l += 1
                chars[l] = cnt_str[tmp]
                tmp += 1
            res += (len(str(cnt)) + 1)
        else:
            res += 1
        return res

