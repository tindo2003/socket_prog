from typing import List
from collections import defaultdict


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
    # For each segment in `pieces`, check if it can be constructed by consecutive elements in `arr`.
    # Specifically:
    # - The first element of the segment must exist in `arr`.
    # - The subsequent elements of the segment (if any) must appear in `arr` immediately after the previous element, maintaining the same order.
        my_dict = defaultdict(int)
        for idx, val in enumerate(arr):
            my_dict[val] = idx
        for piece in pieces:
            first_ele = piece[0]
            if first_ele not in my_dict:
                return False
            first_idx = my_dict[first_ele]
            next_idx = first_idx + 1
            for next_ele in piece[1:]:
                if next_ele not in my_dict:
                    return False
                if my_dict[next_ele] != next_idx:
                    return False
                next_idx += 1

        return True
