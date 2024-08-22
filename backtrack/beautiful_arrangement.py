class Solution:    
    def countArrangement(self, n: int) -> int:
            self.ans = 0
            arr = [i for i in range(1, n + 1)]
            
            def helper(idx):
                if idx >= n:
                    self.ans += 1
                    return
                for new_idx in range(idx, n):
                    swap(arr, idx, new_idx)
                    if arr[idx] % (idx+1) == 0 or (idx+1) % arr[idx] == 0:
                        helper(idx + 1)
                    swap(arr, idx, new_idx)
                
            
            def swap(arr, i:int, j:int):
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
            helper(0)
            return self.ans