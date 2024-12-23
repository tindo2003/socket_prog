class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1, N2 = len(s), len(t)
        ptr1, ptr2 = 0, 0
        while ptr1 < N1:
            cur_ele = s[ptr1]
            while ptr2 < N2 and cur_ele != t[ptr2]:
                ptr2 += 1
            if ptr2 >= N2 and ptr1 < N1:
                return False
            ptr2 += 1
            ptr1 += 1
        return True
