# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n + 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid - 1
                ans = mid 
            else:
                l = mid + 1
        return ans
