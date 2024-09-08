from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head 
        dummy = Node(-1)
        tmp = dummy
        my_dict = {} # old node: new node
        while cur is not None:
            new_node = Node(cur.val) 
            my_dict[cur] = new_node
            cur = cur.next
            tmp.next = new_node 
            tmp = tmp.next 
        cur = head 
        
        while cur is not None:
            new_equivalent = my_dict[cur]
            random = cur.random 
            if random:
                random_equivalent = my_dict[random]
                new_equivalent.random = random_equivalent
            cur = cur.next
        return dummy.next
        