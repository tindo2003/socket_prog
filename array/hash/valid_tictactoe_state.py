from typing import List
from collections import defaultdict


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        num_x = num_o = 0
        N, M = len(board), len(board[0])
        x_moves = defaultdict(int)
        o_moves = defaultdict(int)
        for r in range(N):
            for c in range(M):
                r_key = f"r_{r}"
                c_key = f"c_{c}"
                if board[r][c] == "X":
                    x_moves[r_key] += 1
                    x_moves[c_key] += 1
                    if r == c:
                        x_moves["major"] += 1
                    if (
                        (r == 0 and c == 2)
                        or (r == 1 and c == 1)
                        or (r == 2 and c == 0)
                    ):
                        x_moves["minor"] += 1
                    num_x += 1
                elif board[r][c] == "O":
                    o_moves[r_key] += 1
                    o_moves[c_key] += 1
                    if r == c:
                        o_moves["major"] += 1
                    if (
                        (r == 0 and c == 2)
                        or (r == 1 and c == 1)
                        or (r == 2 and c == 0)
                    ):
                        o_moves["minor"] += 1
                    num_o += 1

        x_won = o_won = False
        for k, v in x_moves.items():
            if v == 3:
                x_won = True
                break
        for k, v in o_moves.items():
            if v == 3:
                o_won = True
                break

        first = not (x_won and o_won)
        second = 0 <= num_x - num_o <= 1

        # if x won, o can't move
        if x_won:
            return (num_x - num_o == 1) and first
        # if o won, x can't move
        if o_won:
            return num_x - num_o == 0 and first
        return first and second
