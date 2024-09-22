from typing import List
from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # special cols: 
        ans = 0
        my_dict = defaultdict(set)
        for x,y in reservedSeats:
            my_dict[x].add(y)
        for col_set in my_dict.values():
            cur_state = 7
            for col in col_set:
                if col in [4, 5]:
                    cur_state &= 1
                if col in [6, 7]:
                    cur_state &= 4
                if col in [2, 3]:
                    cur_state &= 3
                if col in [8, 9]:
                    cur_state &= 6
            if cur_state == 7 or cur_state == 5: ans += 2
            elif cur_state != 0:
                ans += 1
        ans += (2 * (n - len(my_dict)))
        return ans


                



