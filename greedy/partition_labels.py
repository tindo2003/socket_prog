from typing import List
from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # objective: merge intervals. extend the tail if found an overlapping interval with longer tail
        my_dict = defaultdict(
            lambda: [float("inf"), float("-inf")]
        )  # Default values: [min_index, max_index]

        for i, c in enumerate(s):
            my_dict[c][0] = min(my_dict[c][0], i)
            my_dict[c][1] = max(my_dict[c][1], i)

        itvs = list(my_dict.values())
        itvs.sort(key=lambda x: x[0])
        stack = [itvs[0]]
        for s, e in itvs[1:]:
            if stack:
                s1, e1 = stack[-1]
                if s < e1:
                    stack.pop()
                    stack.append((s1, max(e, e1)))
                else:
                    stack.append((s, e))
        tmp = [e - s + 1 for s, e in stack]
        return tmp
