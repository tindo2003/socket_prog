import math 
from typing import List 
from collections import deque 
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = math.floor(math.log(label, 2))
        res = deque([label])

        while level > 0:
            parent = label // 2
            prev_level = level - 1

            start_val = int(2**prev_level)  
            number_of_nodes = start_val

            idx = parent - start_val
            label = start_val + (number_of_nodes - idx) - 1
            res.appendleft(label)

            level -= 1
        return res