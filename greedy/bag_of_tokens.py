from typing import List
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        res = 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
            else:
                if score <= 0: break 
                score -= 1
                power += tokens[r]
                r -= 1
            res = max(res, score)
        return res

