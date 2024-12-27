from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # pretty much the same as non_overlapping_intervals. length of longest chain = minimum of intervals need to be removedm
        pairs.sort(key=lambda x: x[1])
        stack = [pairs[0]]
        for s, e in pairs[1:]:
            if stack:
                s1, e1 = stack[-1]
                if s <= e1:
                    continue
                else:
                    stack.append((s, e))
        return len(stack)
