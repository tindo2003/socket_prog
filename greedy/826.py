from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        lst = []
        for idx in range(n):
            lst.append((profit[idx], difficulty[idx]))
        
        lst.sort(reverse=True)
        worker.sort(reverse=True)
        
        res = 0
        ptr = 0
        for x in worker:
            while ptr < n and x < lst[ptr][1]:
                ptr += 1
            if ptr >= n:
                break 
            res += lst[ptr][0]
        return res



def main():
    sol = Solution()
    difficulty = [2,4,6,8,10]
    profit = [60,20,30,40,50]
    worker = [4,5,6,7]
    res = sol.maxProfitAssignment(difficulty, profit, worker)
    print(res)

if __name__ == "__main__":
    main()