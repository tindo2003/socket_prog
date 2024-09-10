# Definition for singly-linked list.
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  
        current = 0
        r, c = 0, -1
        new_board = [[-1] * n for _ in range(m)]
        cur = head
        while cur is not None:
            dr, dc = directions[current]
            nr, nc = r + dr, c + dc 
            if 0 <= nr < m and 0 <= nc < n and new_board[nr][nc] == -1:
                new_board[nr][nc] = cur.val
                cur = cur.next
                r, c = nr, nc 
            else:
                current = (current + 1) % 4 
        return new_board


      

                 