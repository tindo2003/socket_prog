class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(string):
            return string[::-1]

        def invert(string):
            for idx, c in enumerate(string):
                if c == "0": string[idx] = "1"
                else: string[idx] = "0"
            return string
            
        def dfs(cur_num) -> list[str]:
            if cur_num == 1: return ["0"]
            prev_lst = dfs(cur_num - 1)
            return prev_lst + ["1"] + reverse(invert(prev_lst))        
        
        res = dfs(n)
        return res[k-1]