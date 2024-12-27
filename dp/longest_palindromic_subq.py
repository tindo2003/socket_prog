class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        the trick is to have another string by reversing the input string. then lcs on both input string and new string
        """

        def lcs(s1: str, s2: str) -> int:
            N1 = len(s1)
            N2 = len(s2)
            dp = [[0] * (N1 + 1) for _ in range(N2 + 1)]
            for i in range(1, N1 + 1):
                for j in range(1, N2 + 1):
                    if s1[i - 1] == s2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            return dp[-1][-1]

        return lcs(s, s[::-1])
