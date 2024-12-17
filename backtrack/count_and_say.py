class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1)
        cnt = 1
        res = ""
        for idx in range(len(s) - 1):
            if s[idx] != s[idx + 1]:
                res += str(cnt)
                res += s[idx]
                cnt = 0
            cnt += 1
        res += str(cnt)
        res += s[len(s) - 1]
        return res
