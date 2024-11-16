from typing import List 
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # Each boat carries at most two people at the same time
        l, r = 0, len(people) - 1
        res = 0
        while l <= r:
            if l == r:
                res += 1
                break
            s = people[l] + people[r]
            if s > limit:
                r -= 1
            else:
                r -= 1 
                l += 1
            res += 1
        return res