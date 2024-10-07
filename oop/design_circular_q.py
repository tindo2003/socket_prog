class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

class LL:
    def __init__(self, limit):
        self.head = None  
        self.tail = None  
        self.size = 0
        self.limit = limit 
    
    def insert_head(self, val) -> bool:
        if self.size >= self.limit: return False
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node 
        self.tail = new_node 
        self.tail.next = self.head 
        self.size += 1
        return True 
    
    def get_head(self) -> int:
        return self.head.val 

    def get_tail(self) -> int:
        return self.tail.val

    def remove_head(self) -> bool:
        if not self.head: return False 
        if self.head == self.tail: 
            self.head = None 
            self.tail = None 
        if self.head.next:
            next_head = self.head.next
            self.head = next_head 
            self.tail.next = self.head 
            self.size -= 1
        return True  
        self.size -= 1
    
    def is_empty(self) -> bool:
        return self.head 

    def is_full(self):
        return self.size == self.limit

class MyCircularQueue:
    '''initilize q of size k''' 
    def __init__(self, k: int):
        self.ll = LL(k) 
    def enQueue(self, value: int) -> bool:
        return self.ll.insert_head(value)

    def deQueue(self) -> bool:
        return self.ll.remove_head()

    def Front(self) -> int:
        '''front of the q'''
        return self.ll.get_head()
    
    def Rear(self) -> int:
        '''back of the q'''
        return self.ll.get_tail()
    
    def isEmpty(self) -> bool:
        '''whether or not q is empty''' 
        return self.ll.is_empty()

    def isFull(self) -> bool:
        return self.ll.is_full()