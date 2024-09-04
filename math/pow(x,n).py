class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        want to calculate x^n
        3^4 = 9^2
        3^5 = 3 * 3^4
        2^10 = 4^5 = 4 * 4^4 = 4 * 16^2 = 4 * 16 * 16^1 = 4 * 16 * 16 * 1 = 
        '''
        
        def recur(cur_x, cur_n):
            nonlocal x
            if cur_n == 0:
                return 1
            if cur_n % 2 == 0:
                return recur(cur_x * cur_x, cur_n / 2)
            else:
                return cur_x * recur(cur_x, cur_n - 1)
        res = recur(x, abs(n))
        if n < 0: return 1/res
        else: return res

def main():
    sol = Solution()
    x = 2
    n = 10 
    res = sol.myPow(x, n)
    print(res)

if __name__ == "__main__":
    main()