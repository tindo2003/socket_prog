from typing import List, Optional

class Node:
    def __init__(self) -> None:
        self.edges = {}
        self.words = []

    def add(self, word):
        self.words.append(word)
        self.words.sort()
        if len(self.words) > 3:
            self.words.pop()

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        current = self.root 
        for c in word:
            if c not in current.edges:
                current.edges[c] = Node()
            current = current.edges[c]
            current.add(word)
    
    def searchWithPrefix(self, word):
        ans = []
        current = self.root

        for c in word:
            if c not in current.edges:
                break 
            current = current.edges[c]
            ans.append(current.words)

        while(len(ans) < len(word)):
            ans.append([])
        
        return ans
    
    def printTrie(self):
        cur = self.root
        def helper(cur, prefix):
            print(f"my words at prefix {prefix}: {cur.words}")
            for char, node in cur.edges.items():
                tmp = prefix + char
                helper(node, tmp)
        helper(cur, "")


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()

        for product in products:
            t.add(product)
        t.printTrie()
        return t.searchWithPrefix(searchWord)

         
def main():
    sol = Solution()
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mouse"
    res = sol.suggestedProducts(products, searchWord)
    print(res)

if __name__ == "__main__":
    main()