class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        N = len(s)
        res = [inf] * N
        l = -1
        for i in range(N):
            if s[i] == c:
                l = i 
                res[i] = 0
            else:
                if l >= 0:
                    res[i] = i - l
        r = -1
        for i in range(N-1, -1, -1):
            if s[i] == c:
                r = i 
            else:
                if r >= 0:
                    res[i] = min(res[i], r - i)
        return res