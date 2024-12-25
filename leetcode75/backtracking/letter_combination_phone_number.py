from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        number_to_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(cur: int, lst: List[chr]):
            if cur >= len(digits):
                res.append("".join(lst))
                return
            cur_num = digits[cur]
            possible_letters = number_to_letters[cur_num]
            for letter in possible_letters:
                lst.append(letter)
                dfs(cur + 1, lst)
                lst.pop()

        dfs(0, [])
        return res
