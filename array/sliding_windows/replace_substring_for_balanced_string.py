from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        print(counter)
        l = 0
        N = len(s)
        res = inf
        target = N // 4
        for r in range(N):
            cur_ele = s[r]
            counter[cur_ele] -= 1
            while (l < N and counter['Q'] <= target and 
                   counter['W'] <= target and 
                   counter['E'] <= target and 
                   counter['R'] <= target):
                res = min(res, r - l + 1)
                counter[s[l]] += 1
                l += 1 