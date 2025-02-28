from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        words = set(wordDict)

        def recur(l, r, cur_lst):
            nonlocal res
            if r == len(s):
                if s[l:r] in words:
                    cur_lst.append(s[l:r])
                    res.append(" ".join(cur_lst))
                    cur_lst.pop()
                return
            if s[l:r] in words:
                cur_lst.append(s[l:r])
                recur(r, r + 1, cur_lst)
                cur_lst.pop()
                recur(l, r + 1, cur_lst)
            else:
                recur(l, r + 1, cur_lst)

        recur(0, 0, [])
        return res
