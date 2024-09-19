class Node:
    def __init__(self):
        self.edges = {} # alphabet -> Node
        self.value = 0

class Trie:
    def __init__(self):
        self.root = None 
    
    def insert_key_val(self, key: str, val: int):
        if not self.root:
            self.root = Node()
        cur = self.root
        for c in key:
            if c not in cur.edges:
                cur.edges[c] = Node()
            cur = cur.edges[c]
        cur.value = val
    
    def find_sum_with_same_pref(self, prefix: str):
        cur = self.root 
        res = 0
        for c in prefix:
            if c not in cur.edges:
                return res
            cur = cur.edges[c]
        def dfs(cur):
            nonlocal res
            for neighbor, val in cur.edges.items():
                res += val
                dfs(neighbor)
        dfs(cur)
        return res



class MapSum:

    def __init__(self):
        self.my_trie = Trie()
        

    def insert(self, key: str, val: int) -> None:
        self.my_trie.insert_key_val(key, val)
        

    def sum(self, prefix: str) -> int:
        return self.my_trie.find_sum_with_same_pref(prefix)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)