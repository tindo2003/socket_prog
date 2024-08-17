from typing import List

class Solution:
    def match(self, word, pattern) -> bool:
        lookup = {}
        rlookup = {}
        for a, b in zip(word, pattern):
            if a in lookup:
                if lookup[a] != b:
                    return False 
            if b in rlookup:
                if rlookup[b] != a:
                    return False 
        lookup[a] = b
        rlookup[b] = a
        return True 
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        tmp = []
        for word in words:
            if self.match(word, pattern):
                tmp.append(word)
        return tmp
