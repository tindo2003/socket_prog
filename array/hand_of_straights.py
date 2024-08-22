from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool: 
        my_counter = Counter(hand)
        for key in sorted(my_counter.keys()):
            # key observation is we want to start at the smallest ele until we exhaust it
            while my_counter[key] != 0:
                idx = 0
                while idx < groupSize:
                    if my_counter[key + idx] == 0:
                        return False
                    idx += 1
                idx = 0
                while idx < groupSize:
                    my_counter[key + idx] -= 1
                    idx += 1
        return True