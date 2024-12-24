class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        ptr1 = ptr2 = 0
        N = len(word1)
        M = len(word2)
        while ptr1 < N and ptr2 < M:
            res.append(word1[ptr1])
            res.append(word2[ptr2])
            ptr1 += 1
            ptr2 += 1
        if ptr1 < N:
            res += word1[ptr1:]
        if ptr2 < M:
            res += word2[ptr2:]
        return "".join(res)
