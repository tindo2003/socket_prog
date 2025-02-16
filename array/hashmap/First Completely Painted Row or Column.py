class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        row_left = {i: m for i in range(n)}
        column_left = {i: n for i in range(m)}
        my_dict = defaultdict(tuple)
        for r in range(n):
            for c in range(m):
                my_dict[mat[r][c]] = (r, c)
        for idx, ele in enumerate(arr):
            r, c = my_dict[ele]
            row_left[r] -= 1
            column_left[c] -= 1
            if row_left[r] == 0 or column_left[c] == 0:
                return idx
