from typing import List 
from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        my_dict = defaultdict(int)
        res = 0 
        for t in time: 
            for num in range(60, 500, 60):
                wanted_num = num - t 
                if wanted_num in my_dict:
                    res += my_dict[wanted_num]
            my_dict[t] += 1
        return res

'''
alternative
'''
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        my_arr = [0] * 61
        res = 0
        for t in time:
            mod = t % 60
            if mod == 0:
                res += my_arr[0]
            else:
                res +=  my_arr[60-mod]
            my_arr[mod] += 1
        return res
        