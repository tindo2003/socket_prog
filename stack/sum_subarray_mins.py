from typing import List 

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)

        pse = [0] * n 
        nse = [0] * n 
        MOD = 10**9 + 7
        
        def generate_nse(stack):
            for idx in range(n-1, -1, -1):
                cur_ele = arr[idx]
                
                while stack:
                    top = stack[-1]
                    if cur_ele <= arr[top]:
                        stack.pop()
                        continue 
                    if cur_ele > arr[top]:
                        break 
                if not stack:
                    nse[idx] = n 
                else:
                    nse[idx] = stack[-1]
                stack.append(idx)

        def generate_pse(stack):
            for idx in range(n):
                cur_ele = arr[idx]
                while stack:
                    top = stack[-1]
                    if cur_ele < arr[top]:
                        stack.pop()
                        continue 
                    if cur_ele >= arr[top]:
                        break 
                if not stack:
                    pse[idx] = -1
                else:
                    pse[idx] = stack[-1]
                stack.append(idx)
        generate_nse([])
        print(nse)
        generate_pse([])
        print(pse)
        total = 0
        for idx, val in enumerate(arr):
            left = idx - pse[idx]
            right = nse[idx] - idx
            total += (val * left * right)
            #print(f"left: {left}; right: {right}; total: {total}")
            total %= MOD 
        return total
        

def main():
    sol = Solution()
    arr = [11,81,94,43,3]
    res = sol.sumSubarrayMins(arr)
    print(res)

if __name__== "__main__":
    main()

            

