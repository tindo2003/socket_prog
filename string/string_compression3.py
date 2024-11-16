class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        N = len(word)
        idx = 0 
        while idx < N:
            prev_char = word[idx]
            cnt = 1
            while idx + 1 < N and word[idx] == word[idx + 1] and cnt < 9:
                cnt += 1
                idx += 1
            else: 
                idx += 1
            res.append(str(cnt))
            res.append(prev_char)
        return "".join(res)