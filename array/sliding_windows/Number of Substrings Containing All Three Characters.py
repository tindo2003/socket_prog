from math import inf


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        # character -> idx
        my_dict = {"a": -1, "b": -1, "c": -1}

        def check_good():
            mini = inf
            for k, v in my_dict.items():
                if mini == inf:
                    mini = v
                else:
                    mini = min(mini, v)
                if v < 0:
                    return (False, None)
            return (True, mini)

        res = 0
        for r in range(n):
            my_dict[s[r]] = r
            good, min_index = check_good()
            if good:
                res += min_index - 0 + 1
        return res
