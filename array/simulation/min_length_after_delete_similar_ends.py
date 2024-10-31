class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r:
            new_l = s[l]
            new_r = s[r]
            old_l = l
            old_r = r
            while l + 1 < len(s) and s[l] == s[l + 1]:
                l += 1
            while r - 1 >= 0 and s[r] == s[r - 1]:
                r -= 1
            if new_l != new_r: 
                return old_r - old_l + 1
            l += 1
            r -= 1
        if l == r: return 1
        return 0
        
            
