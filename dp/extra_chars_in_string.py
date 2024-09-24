from typing import List
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dict_set = set(dictionary)
        N = len(s)
        cache = {}
        def dfs(cur_idx) -> int:
            if cur_idx == N: return 0
            res = float("inf")
            if cur_idx in cache: return cache[cur_idx]
            for next_idx in range(cur_idx + 1, N+1):
                cur = 0
                do_work = dfs(next_idx)
                if s[cur_idx : next_idx] in dict_set:
                    cur = do_work
                else:
                    cur = (next_idx - cur_idx) + do_work
                res = min(res, cur)
            cache[cur_idx] = res
            return cache[cur_idx]
        return dfs(0)

def main():
    sol = Solution()
    s = "leetscode"
    dictionary = ["leet","code","leetcode"]
    res = sol.minExtraChar(s, dictionary)
    print(res)

if __name__ == "__main__":
    main()

        