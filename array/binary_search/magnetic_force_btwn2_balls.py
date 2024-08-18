from typing import List 

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        N = len(position)
        def can_place(distance) -> bool:
            bags = 1
            cur = 0
            for idx in range(1, N):
                pos = position[idx]
                if position[cur] + distance <= pos:
                    cur = idx
                    bags += 1 
            return bags >= m
        l = 0 
        r = position[-1] - position[0] + 1
        while r - l > 1:
            mid = (l + r) // 2 

            if can_place(mid):
                l = mid 
            else:
                r = mid 
        return l

def main():
    sol = Solution()
    position = [5,4,3,2,1,1000000000]
    m = 2
    res = sol.maxDistance(position, m)
    print(res)

if __name__ == "__main__":
    main()
