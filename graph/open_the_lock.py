from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        best = {}
        visited = set(["0000"])
        q = ["0000"]
        best["0000"] = 0
        while q:
            cur = q.pop(0)
            if cur == target:
                return best[cur]
            list_cur = list(cur)
            for i in range(4):
                for direc in [1, -1]:
                    old_val = list_cur[i]
                    tmp_val = int(old_val) + direc
                    if tmp_val < 0:
                        list_cur[i] = "9"
                    elif tmp_val > 9:
                        list_cur[i] = "0"
                    else:
                        list_cur[i] = str(tmp_val)
                    my_str = "".join(list_cur)
                    if my_str not in visited and my_str not in deadends:
                        best[my_str] = best[cur] + 1
                        visited.add(my_str)
                        q.append(my_str)
                    list_cur[i] = old_val
        return -1


def main():
    sol = Solution()
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    res = sol.openLock(deadends, target)
    print(res)


if __name__ == "__main__":
    main()
