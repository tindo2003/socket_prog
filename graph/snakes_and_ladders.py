from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N, M = len(board), len(board[0])
        def convert_to_rc(num):
            num -= 1
            r = num // M
            c = num % M 
            if r % 2 == 1:
                c = M - 1 - c 
            r = N - r  - 1
            return (r, c)
        r, c = convert_to_rc(31)
        visited = set()
        
        q = deque([(1, 0)])
        
        while q:
            cur, moves = q.popleft()
            
            for neighbor in range(cur + 1, min(cur + 7, N**2+1)):
                if neighbor not in visited:
                    visited.add(neighbor)
                    r, c = convert_to_rc(neighbor)
                    if board[r][c] != -1:
                        neighbor = board[r][c]
                    if neighbor == N**2: return moves + 1
                    q.append((neighbor, moves + 1))
        return -1