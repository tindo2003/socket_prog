class Solution:
    def findNthDigit(self, n: int) -> int:

        num_digit = 1
        count = 9
        
        while n > num_digit * count:
            n = n - (num_digit * count)
            num_digit += 1
            count *= 10 
        
        start_num = 10**(num_digit-1)
        
        
        ith_since_start, remainder = divmod(n, num_digit)
        
        if remainder == 0:
            return int(str(start_num + ith_since_start - 1)[-1])
        else:
            return int(str(start_num + ith_since_start)[remainder-1])