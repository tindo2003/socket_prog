class Solution:
    def checkValidString(self, s: str) -> bool:
        # trick: do 2 stacks
        star = []
        open = []
        for idx, ele in enumerate(s):
            if ele == "*":
                star.append(idx)
            elif ele == "(":
                open.append(idx)
            elif ele == ")":
                # we always pop open first cuz we wanna reserve star cuz it has more options
                if open:
                    open.pop()
                elif star:
                    star.pop()
                else:
                    return False
        # it doesn't matter if star is empty or not.
        while open:
            if not star:
                return False
            cur_star_idx = star.pop()
            cur_open_idx = open.pop()
            # star has to come after ( because else, we can't satisfy it. *( becomes )( or (( or ( by itself won't work. when star comes after (, it becomes )
            if cur_star_idx < cur_open_idx:
                return False
        return True
