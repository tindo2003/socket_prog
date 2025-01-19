class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # TWO PTR: MOVE ALL ZEROS TO THE LEFT
        s_lst = list(s)
        N = len(s_lst)
        prev_zero = 0
        for r in range(N):
            if s[r] != "0":
                s_lst[prev_zero] = s[r]
                prev_zero += 1
        for i in range(prev_zero, N):
            s_lst[i] = "0"

        # MAKE SURE THE LAST ELEMENT IS 1 SO THAT IT IS AN ODD NUMBER
        s_lst[prev_zero - 1] = "0"
        s_lst[N - 1] = "1"
        return "".join(s_lst)
