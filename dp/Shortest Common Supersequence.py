class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        variation of LCS problem
        """
        n, m = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[j - 1] == str2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        str1_indices = []
        str2_indices = []
        r, c = m, n
        while r >= 0 and c >= 0:
            if dp[r][c] != dp[r - 1][c] and dp[r][c] != dp[r][c - 1]:
                str1_indices.append(c - 1)
                str2_indices.append(r - 1)
                r -= 1
                c -= 1
            else:
                if dp[r][c] == dp[r - 1][c]:
                    r -= 1
                else:
                    c -= 1
        l_idx1, l_idx2 = 0, 0
        r_idx1, r_idx2 = 0, 0
        s = []
        str1_indices = str1_indices[::-1]
        str2_indices = str2_indices[::-1]
        for i in range(len(str1_indices)):
            r_idx1 = str1_indices[i]
            r_idx2 = str2_indices[i]
            while l_idx1 < r_idx1:
                s.append(str1[l_idx1])
                l_idx1 += 1
            while l_idx2 < r_idx2:
                s.append(str2[l_idx2])
                l_idx2 += 1
            s.append(str1[l_idx1])
            l_idx1 += 1
            l_idx2 += 1
        s.append(str1[l_idx1 : len(str1)])
        s.append(str2[l_idx2 : len(str2)])
        return "".join(s)
