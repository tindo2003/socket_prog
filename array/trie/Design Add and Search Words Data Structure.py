class Node:
    def __init__(
        self,
    ):
        self.is_end = False
        self.edges = {}  # dict of c -> Node


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.edges:
                cur.edges[c] = Node()
            cur = cur.edges[c]
        cur.is_end = True

    def search(self, word: str) -> bool:

        def dfs(cur_node, idx):
            if idx == len(word):
                return cur_node.is_end == True
            cur_char = word[idx]
            found = False
            if word[idx] == ".":
                for c in cur_node.edges.keys():
                    if dfs(cur_node.edges[c], idx + 1):
                        # if found one possibility, no need to go further
                        found = True
                        break
            else:
                if cur_char in cur_node.edges:
                    found = dfs(cur_node.edges[cur_char], idx + 1)
            return found

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
