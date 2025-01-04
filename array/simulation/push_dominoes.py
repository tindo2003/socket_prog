from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # SIMULATION. watch neetcode
        dom_lst = list(dominoes)
        q = deque([])
        N = len(dominoes)
        for idx, item in enumerate(dom_lst):
            if item in ["R", "L"]:
                q.append((item, idx))
        while q:
            direction, idx = q.popleft()
            if direction == "R":
                if idx + 1 < N and dom_lst[idx + 1] == ".":
                    if idx + 2 < N and dom_lst[idx + 2] == "L":
                        q.popleft()
                    else:
                        dom_lst[idx + 1] = "R"
                        q.append(("R", idx + 1))
            elif direction == "L":
                if idx - 1 >= 0 and dom_lst[idx - 1] == ".":
                    dom_lst[idx - 1] = "L"
                    q.append(("L", idx - 1))
        return "".join(dom_lst)
