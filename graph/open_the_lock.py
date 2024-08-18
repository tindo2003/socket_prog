from typing import List
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        forbidden = set(deadends)
        if target == "0000":
            return 0
        if "0000" in forbidden or target in forbidden:
            return -1
        q = deque()
        best = {}

        q.append("0000")
        best["0000"] = 0

        while q:
            now = q.popleft()

            for i in range(4):
                for d in [1, -1]:
                    cur_dig = int(now[i])
                    cur_dig += d 
                    cur_dig %= 10 
                    nxt_dig = now[:i] + str(cur_dig) + now[i+1:]

                    if nxt_dig in forbidden:
                        continue 
                    
                    if nxt_dig in best:
                        continue 
                    
                    if nxt_dig == target:
                        return best[now] + 1
                    best[nxt_dig] = best[now] + 1
                    q.append(nxt_dig)
        return -1 

def main():
    sol = Solution()
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    res = sol.openLock(deadends, target)
    print(res)

if __name__ == "__main__":
    main()