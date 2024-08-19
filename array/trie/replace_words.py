from typing import List, Optional

class TreeNode:
    def __init__(self):
        self.edges = {}
        self.is_root = False 

class Trie:
    def __init__(self):
        self.root = None 
    
    def add_word(self, word):
        if not self.root:
            self.root = TreeNode()
        cur = self.root 
        for idx, c in enumerate(word):
            if c not in cur.edges:
                cur.edges[c] = TreeNode()
            cur = cur.edges[c]
            if idx == len(word) - 1:
                cur.is_root = True 
    
    def search_root(self, word) -> Optional[str]:
        cur = self.root
        for idx, c in enumerate(word):
            if cur.is_root:
                return word[:idx]
            if c not in cur.edges:
                return None 
            cur = cur.edges[c]


class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # replace it with the root that has the shortest length.
        my_trie = Trie()
        for word in dictionary:
            my_trie.add_word(word)
        res = []
        words = sentence.split(" ")
        for word in words:
            tmp = my_trie.search_root(word)
            #print(tmp)
            if tmp:
                res.append(tmp)
            else:
                res.append(word)
        return " ".join(res)


def main():
    sol = Solution()
    dictionary = ["a","b","c"]
    sentence = "aadsfasf absbs bbab cadsfafs"
    res = sol.replaceWords(dictionary, sentence)
    print(res)

if __name__ == "__main__":
    main()