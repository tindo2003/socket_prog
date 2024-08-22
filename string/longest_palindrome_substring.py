
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        best_len = -inf
        best_str = ""
        
        for mid in range(N):
            x = 0
            while mid - x >= 0 and x + mid < N:
                if s[mid - x] != s[mid + x]:
                    break 
                # for example, if mid = 3, then mid - x = 1, mid + x = 5
                cur_len = 2 * x + 1
                if cur_len > best_len:
                    best_len = cur_len
                    best_str = s[mid - x : mid + x +1]
                x += 1
            
        for mid in range(N):
            x = 1
            # first: compare the mid & mid + 1
            # snd: compare mid - 1 and mid + 2
            # third: compare mid - 2 and mid + 3
            while mid - x + 1 >= 0 and mid + x < N:
                if s[mid - x + 1] != s[x+mid]:
                    break 
                cur_len = 2 * x
                if cur_len > best_len:
                    best_len = cur_len
                    best_str = s[mid - x + 1: mid + x +1]
                x += 1 
        return best_str

def main():
    sol = Solution()
    s = "abba"
    res = sol.longestPalindrome(s)
    print(res)

if __name__ == "__main__":
    main()
