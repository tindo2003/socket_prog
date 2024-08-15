from typing import List 

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = float("-inf")
        for house in houses:
            l = 0 
            r = len(heaters) - 1
            res = float("inf")
            while l <= r:
                mid = (l + r) // 2
                if house < heaters[mid]:
                    r = mid - 1
                elif house > heaters[mid]:
                    l = mid + 1
                else:
                    res = 0
                    break
            if 0 <= l < len(heaters):
                res = min(res, abs(house - heaters[l]))
            if 0 <= r < len(heaters):
                res = min(res, abs(house - heaters[r])) 
            ans = max(ans, res)
        return ans

def main():
    sol = Solution()
    houses = [1, 5]
    heaters = [2]
    res = sol.findRadius(houses, heaters)
    print(res)

if __name__ == "__main__":
    main()
