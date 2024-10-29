from collections import defaultdict
from typing import List


class Node:
    def __init__(self):
        self.isEnd = False
        self.edges = defaultdict(int)


class Trie:
    def __init__(self):
        self.root = None

    def insert(self, string):
        if not self.root:
            self.root = Node()
        cur_node = self.root

        for c in string:
            if c not in cur_node.edges:
                cur_node.edges[c] = Node()
            cur_node = cur_node.edges[c]
        cur_node.isEnd = True

    def get_result(self, cur_node, cur_str, lst):
        for c, new_node in cur_node.edges.items():
            new_str = cur_str + "/" + c
            if new_node.isEnd:
                lst.append(new_str)
            else:
                self.get_result(new_node, new_str, lst)


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        myTrie = Trie()
        for f in folder:
            spl = f.split("/")[1:]
            myTrie.insert(spl)
        my_lst = []
        myTrie.get_result(myTrie.root, "", my_lst)
        return my_lst
