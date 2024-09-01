class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        string = list(str(n))
        N = len(string)
        idx = 1
        while idx < N:
            if int(string[idx]) < int(string[idx-1]):
                break
            idx += 1
        while 1 <= idx < N and string[idx-1] > string[idx]:
            string[idx] = '9'
            string[idx-1] = str(int(string[idx-1]) - 1)
            idx -= 1
        
        for i in range(idx + 1, N):
            string[i] = '9'
        return int("".join(string))