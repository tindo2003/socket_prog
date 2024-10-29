class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        my_dict = defaultdict(deque)
        N = len(mat)
        M = len(mat[0])
        for r in range(N):
            for c in range(M):
                diag = r + c
                if diag % 2 == 1:
                    my_dict[diag].append(mat[r][c])
                else:
                    my_dict[diag].appendleft(mat[r][c])
        res = []
        for deq in my_dict.values():
            res = res + list(deq)
        return res
