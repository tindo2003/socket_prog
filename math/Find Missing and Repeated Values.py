from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # 1 + 2 + 3 + 4
        # 1 + 3 + 2+ 2
        my_set = set()
        n = len(grid)
        repeated_ele = -1
        actual_s = 0
        for r in range(n):
            for c in range(n):
                cur_ele = grid[r][c]
                if cur_ele in my_set:
                    repeated_ele = cur_ele
                my_set.add(cur_ele)
                actual_s += cur_ele
        d = 1
        a = 1
        n1 = n * n
        expected_s = (n1 / 2) * (2 * a + (n1 - 1) * d)
        d = expected_s - actual_s
        return [repeated_ele, int(d + repeated_ele)]
