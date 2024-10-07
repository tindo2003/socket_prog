class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[-1] * n for _ in range(4)]

        '''
        at a column idx, there are 4 possible choices. 
        1. both rows are empty  0
        2. top row filled   1
        3. bottom row filled 2
        4. both rows filled 3
        '''
        def make_state(v1, v2):
            cur = 0 
            if v1: cur |= 1 # 01
            if v2: cur |= 2 # 10
            return cur 
        
        def dfs(col_idx, v1, v2):
            if col_idx == n:
                return 1
            current_state = make_state(v1, v2)
            if dp[current_state][col_idx] != -1: return dp[current_state][col_idx] 
            v3, v4 = col_idx + 1 < n, col_idx + 1 < n 
            count = 0
            if not v1 and not v2:
                count += dfs(col_idx + 1, True, True)
            elif not v1 and v2:
                if v3 and v4:
                    count += dfs(col_idx + 1, False, False)
                    count += dfs(col_idx + 1, False, True)
            elif v1 and not v2:
                if v3 and v4:
                    count += dfs(col_idx + 1, False, False)
                    count += dfs(col_idx + 1, True, False)
            elif v1 and v2: 
                count += dfs(col_idx + 1, True, True)
                if v3 and v4:
                    count += dfs(col_idx + 1, False, True)
                    count += dfs(col_idx + 1, True, False)
                    count += dfs(col_idx + 1, False, False)
            dp[current_state][col_idx] = count
            return count 

        return dfs(0, True, True) % MOD# 

def main():
    sol = Solution()
    n = 4
    res = sol.numTilings(n)
    print(res)

if __name__ == "__main__":
    main()
