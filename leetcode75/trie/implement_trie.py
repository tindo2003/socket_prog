from collections import defaultdict


class Node:
    def __init__(self):
        self.is_end = False
        self.edges = defaultdict(Node)


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.edges:
                cur.edges[c] = Node()
            cur = cur.edges[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.edges:
                return False
            cur = cur.edges[c]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.edges:
                return False
            cur = cur.edges[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
