class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
       self.key = key
       self.val = val
       self.prev = prev
       self.next = next 
class DLL:
    def __init__(self):
        self.head = None 
        self.tail = None
    
    def move_node_to_head(self, node):
        if node != self.head:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            if next_node: 
                next_node.prev = prev_node
            node.next = self.head
            self.head.prev = node 
            self.head = node
            if node == self.tail:
                self.tail = prev_node
        
class LRUCache:

    def __init__(self, capacity: int):
       self.size = capacity 
       self.map = {}
       self.list = DLL()

    def get(self, key: int) -> int:
        # switch to newly accessed node to the front
        if key in self.map:
            node = self.map[key]
            self.list.move_node_to_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # append/switch to the front, remove from the tail 
        if key in self.map:
            self.map[key].val = value 
            # switch to the head
            node = self.map[key]
            self.list.move_node_to_head(node)
        else:
            new_node = Node(key, value)
            if self.list.head is None:
                self.list.head = new_node
                self.list.tail = new_node
            else:
                new_node.next = self.list.head
                self.list.head.prev = new_node 
                self.list.head = new_node
            self.map[key] = new_node
            if len(self.map) > self.size:
                # remove the tail
                tmp = self.list.tail
                prev_node = self.list.tail.prev
                prev_node.next = None
                self.list.tail = prev_node
                del self.map[tmp.key]
        
class LRUCache:

    def __init__(self, capacity: int):
       self.size = capacity 
       self.map = {}
       self.list = DLL()

    def get(self, key: int) -> int:
        # switch to newly accessed node to the front
        if key in self.map:
            node = self.map[key]
            self.list.move_node_to_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # append/switch to the front, remove from the tail 
        if key in self.map:
            self.map[key].val = value 
            # switch to the head
            node = self.map[key]
            self.list.move_node_to_head(node)
        else:
            new_node = Node(key, value)
            if self.list.head is None:
                self.list.head = new_node
                self.list.tail = new_node
            else:
                new_node.next = self.list.head
                self.list.head.prev = new_node 
                self.list.head = new_node
            self.map[key] = new_node
            if len(self.map) > self.size:
                # remove the tail
                tmp = self.list.tail
                prev_node = self.list.tail.prev
                prev_node.next = None
                self.list.tail = prev_node
                del self.map[tmp.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
def main():
   obj = LRUCache(2) 
   obj.put(2, 1)
   obj.put(1, 1)
   obj.put(2, 3)
   obj.put(4, 1)
   obj.get(1)
   obj.get(2)

if __name__ == "__main__":
    main()



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)