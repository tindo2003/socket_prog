class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        N = len(s)
        cnt = 0
        tmp = []
        # count length of consecutive 1s or consecutive 0s and append it to array tmp
        for idx in range(N):
            if idx == 0:
                cnt = 1
            else:
                if s[idx] == s[idx - 1]:
                    cnt += 1
                else:
                    tmp.append(cnt)
                    cnt = 1
        tmp.append(cnt)

        res = 0
        for idx in range(1, len(tmp)):
            res += min(tmp[idx], tmp[idx - 1])
        return res
