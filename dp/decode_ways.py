# inefficient way
class Solution:
    def numDecodings(self, s: str) -> int:
        letter_mapping = {
            "1": 'A', "2": 'B', "3": 'C', "4": 'D', "5": 'E',
            "6": 'F', "7": 'G', "8": 'H', "9": 'I', "10": 'J',
            "11": 'K', "12": 'L', "13": 'M', "14": 'N', "15": 'O',
            "16": 'P', "17": 'Q', "18": 'R', "19": 'S', "20": 'T',
            "21": 'U', "22": 'V', "23": 'W', "24": 'X', "25": 'Y',
            "26": 'Z'
        }
        self.res = 0 
        N = len(s)
        def helper(idx) -> None:
            if idx == N: 
                self.res += 1
                return
            if idx > N: return
            if s[idx] == "0":
                return 
            for offset in [1, 2]:
                new_idx = idx + offset
                if new_idx < N:
                    cur_ele = s[idx:new_idx]
                    if cur_ele in letter_mapping:
                        helper(new_idx)
            
        helper(0)
        return self.res

#efficient way
class Solution:
    def numDecodings(self, s: str) -> int:
        self.res = 0 
        N = len(s)
        
        dp = [0] * (N + 1)
        dp[N] = 1
        if s[-1] != '0':
            dp[N - 1] = 1 

        for i in range(N - 2, -1, -1):
            # Single digit
            if s[i] != '0':
                dp[i] += dp[i + 1]
            
            # Two digits
            two_digit = int(s[i:i+2])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i + 2]
    
        return dp[0]