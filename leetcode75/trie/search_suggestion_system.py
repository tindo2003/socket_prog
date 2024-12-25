from collections import defaultdict, List


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

    def find_products(self, prefix: str) -> List[str]:
        res = []
        cur = self.root
        for c in prefix:
            if c not in cur.edges:
                cur.edges[c] = Node()
            cur = cur.edges[c]

        def dfs(cur, res, cur_str):
            if cur.is_end:
                res.append(cur_str)
            for c, node in cur.edges.items():
                dfs(node, res, cur_str + c)

        dfs(cur, res, prefix)
        return res


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie = Trie()
        res = []
        for product in products:
            trie.insert(product)
        for i in range(len(searchWord)):
            tmp = trie.find_products(searchWord[: i + 1])
            tmp.sort()
            res.append(tmp[:3])
        return res
