class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if mid**2 > x:
                r = mid - 1
            else:
                l = mid + 1
                ans = mid 
        return ans 
