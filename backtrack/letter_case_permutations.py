class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def backtrack(idx, s_lst):
            if idx >= len(s):
                res.append("".join(s_lst))
                return 
            cur_ele = s[idx]
            if cur_ele.isalpha():
                s_lst[idx] = s_lst[idx].upper()
                backtrack(idx + 1, s_lst)
                s_lst[idx] = s_lst[idx].lower()
                backtrack(idx + 1, s_lst)
            else:
                backtrack(idx + 1, s_lst)


        backtrack(0, list(s))
        return res