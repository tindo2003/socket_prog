from typing import List 
class Solution:
    """
    @param board: a 2D integer array
    @return: the current board
    """
    def candy_crush(self, board: List[List[int]]) -> List[List[int]]:
        # Write your code here
        N = len(board)
        M = len(board[0])

        change = False 
        while True:
            
            for r in range(N):
                for c in range(M-2):
                    equal = True
                    for offset in range(1, 3):
                        if board[r][c + offset] == 0 or abs(board[r][c + offset]) != abs(board[r][c + offset - 1]):
                            equal = False
                    if equal:
                        change = True 
                        for offset in range(3):
                            if board[r][c + offset] > 0:
                                board[r][c + offset] *= -1 
            
            for c in range(M):
                for r in range(N-2):
                    equal = True 
                    for offset in range(1,3):
                        if board[r + offset][c] == 0 or abs(board[r + offset][c]) != abs(board[r + offset - 1][c]):
                            equal = False 
                    if equal:
                        change = True 
                        for offset in range(3):
                            if board[r + offset][c] > 0:
                                board[r + offset][c] *= -1 
            
            if not change: 
                break

            # move zeros problem https://leetcode.com/problems/move-zeroes/
            for c in range(M):
                prev_non_zero = N - 1
                for r in range(N-1, -1, -1):
                    if board[r][c] > 0:
                        board[prev_non_zero][c] = board[r][c]
                        prev_non_zero -= 1
                for r in range(prev_non_zero, -1, -1):
                    board[r][c] = 0 
            change = False
            
        return board
                    