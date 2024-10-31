class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1l = list(s1)
        s2l = list(s2)
        s1l.sort()
        s2l.sort()
        good1 = True 
        good2 = True
        for idx in range(len(s1)):
            if s1l[idx] < s2l[idx]: 
                good2 = False
            if s2l[idx] < s1l[idx]: 
                good1 = False
        return good1 or good2