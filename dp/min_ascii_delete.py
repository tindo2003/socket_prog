class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        N = len(s1)
        M = len(s2)
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                actual_i = i - 1
                actual_j = j - 1
                
                if s1[actual_i] == s2[actual_j]:

                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        res = set()
        
        def recur(i, j, cur_str):
            if i == 0 or j == 0:
                res.add(cur_str)
                return 
            actual_i = i - 1
            actual_j = j - 1
            if s1[actual_i] == s2[actual_j]:
                recur(i-1, j-1, cur_str + s1[actual_i])
            else:
                if dp[i][j] == dp[i-1][j]:
                    recur(i-1, j, cur_str)
                if dp[i][j] == dp[i][j-1]:
                    recur(i, j-1, cur_str)
        recur(N, M, "")
        
        s1_ascii = sum([ord(c) for c in s1])
        s2_ascii = sum([ord(c) for c in s2])
        total_ascii = s1_ascii + s2_ascii
        max_ascii = float("-inf")
        for item in res:
            my_str_ascii = sum([ord(c) for c in item])
            max_ascii = max(max_ascii, my_str_ascii)
        return total_ascii - 2 * max_ascii

'''
optimal
''' 
def minimumDeleteSum(self, s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the first row
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j-1] + ord(s2[j-1])

    # Fill the rest of the dp table
    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))

    return dp[m][n]