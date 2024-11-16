class Solution:
    def splitString(self, s: str) -> bool:
        N = len(s)
        def recur(idx, prev_num):
            if idx == -1:
                for new_idx in range(1, N+1):
                    if recur(new_idx, s[0:new_idx]):
                        return True
                return False
            else:
                for new_idx in range(idx+1, N+1):
                    cur_num = int(s[idx:new_idx])
                    if cur_num == int(prev_num) - 1:
                        if new_idx == N: return True
                        if recur(new_idx, cur_num):
                            return True
                return False
        return recur(-1, 0)