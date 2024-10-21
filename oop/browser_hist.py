class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DLL:
    def __init__(self, hp):
        new_node = Node(hp)
        self.head = new_node
        self.cur_loc = new_node
        self.tail = new_node

    def step(self, steps):
        while steps > 0 and self.cur_loc.next:
            steps -= 1
            self.cur_loc = self.cur_loc.next
        return self.cur_loc.val

    def back(self, steps):
        while steps > 0 and self.cur_loc.prev:
            steps -= 1
            self.cur_loc = self.cur_loc.prev
        return self.cur_loc.val

    def insert(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.cur_loc = new_node
        else:
            if self.cur_loc != self.tail:
                self.cur_loc.next = new_node
                new_node.prev = self.cur_loc
                self.cur_loc = new_node
                self.tail = self.cur_loc
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
                self.cur_loc = self.tail


class BrowserHistory:

    def __init__(self, homepage: str):
        self.dll = DLL()

    def visit(self, url: str) -> None:
        self.dll.insert(url)

    def back(self, steps: int) -> str:
        return self.dll.back(steps)

    def forward(self, steps: int) -> str:
        return self.dll.step(steps)


# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory("lc")
obj.visit("google")
obj.visit("facebook")
obj.visit("youtube")
obj.back()
obj.back()
obj.forward()
obj.visit("linkedIn")
obj.forward()
obj.back()
obj.back()
