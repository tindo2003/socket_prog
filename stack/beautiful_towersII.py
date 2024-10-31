from typing import List
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        stack = []
        N = len(maxHeights)
        results = [0] * N
        # monotonic increasing: i < j and maxHeights[stack[j]] > maxHeights[stack[i]]
        for l in range(N):
            cur_num = maxHeights[l]
            while stack:
                top_ele = maxHeights[stack[-1]]
                if cur_num < top_ele:
                    top_idx = stack.pop()
                    results[top_idx] = l - top_idx
                else: break
            stack.append(l)
        while stack:
            idx = stack.pop()
            results[idx] = N - idx
        print(results)

def main():
    sol = Solution()
    arr = [5,3,4,1,1]
    sol.maximumSumOfHeights(arr)

if __name__ == "__main__": 
    main()
