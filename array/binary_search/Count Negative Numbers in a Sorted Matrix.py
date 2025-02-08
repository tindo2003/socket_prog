class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # read the Discussion section about it forming a staircase.
        m = len(grid[0])
        cur_row, cur_col = len(grid) - 1, 0
        res = 0
        while cur_row >= 0:
            while cur_col < m and grid[cur_row][cur_col] >= 0:
                cur_col += 1
            res += m - cur_col
            cur_row -= 1
        return res
