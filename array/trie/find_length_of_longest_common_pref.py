from typing import List
class TrieNode:
    def __init__(self):
        self.edges = {}
        self.is_end = False 
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word) -> None:
        cur = self.root 
        for c in word:
            if c not in cur.edges:
                cur.edges[c] = TrieNode()
            cur = cur.edges[c]
        cur.is_end = True
    
    def add_word_special(self, word) -> int:
        ''' 
        this returns the deepest depth
        '''
        ans = 0 
        cur = self.root 
        
        for idx, c in enumerate(word):
            if c not in cur.edges:
               break 
            cur = cur.edges[c]
            ans = idx + 1
        return ans 


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for num in arr1:
            trie.add_word(str(num))
        res = 0
        for num in arr2:
            res = max(res, trie.add_word_special(str(num)))
        return res 

def main():
    sol = Solution()
    arr1 = [1, 2, 3]
    arr2 = [4, 4, 4]
    res = sol.longestCommonPrefix(arr1, arr2)
    print(res)

if __name__ == "__main__":
    main()

        