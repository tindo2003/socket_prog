class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # TRICK: TWO STACKS AND REPLACE STRING WITH *
        s_lst = list(s)
        for idx, val in enumerate(locked):
            if val == "0":
                s_lst[idx] = "*"
        open_stack = []
        star_stack = []
        for idx, c in enumerate(s_lst):
            if c == ")":
                # PRIORITIZE USING OPEN PARENTHESES CUZ * IS MORE VERSATILE
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            elif c == "(":
                open_stack.append(idx)
            else:
                star_stack.append(idx)

        while open_stack and star_stack:
            open_pos = open_stack.pop()
            star_pos = star_stack.pop()
            if star_pos < open_pos:
                return False
        if open_stack:
            return False
        return len(star_stack) % 2 == 0
