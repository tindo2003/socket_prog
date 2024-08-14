from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False 
        eachPart = total_sum // 3
        cur_sum = 0
        cnt = 0
        for val in arr:
            cur_sum += val 
            if cur_sum == eachPart:
                cur_sum = 0 
                cnt += 1
        return cnt >= 3 

def main():
    sol = Solution()
    arr = [1, 2, 3, 4]
    res = sol.canThreePartsEqualSum(arr)
    print(res)

if __name__ == "__main__":
    main()
