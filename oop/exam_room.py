import heapq

class ExamRoom:
    def calc_dst(self, x, y):
        if x == -1:
            return -y
        elif y == self.N:
            return -(self.N - 1 - x)
        else:
            return -(abs(x-y)//2) 

    def __init__(self, n: int):
        self.q = []
        left = -1
        right = n
        self.N = n
        dst = self.calc_dst(left, right)
        heapq.heappush(self.q, (dst, left, right))

    def seat(self) -> int:
        dst, x, y = heapq.heappop(self.q)
        if x == -1:
            pos = 0
        elif y == self.N:
            pos = self.N - 1
        else:
            pos = (x + y) // 2
        heapq.heappush(self.q, (self.calc_dst(x, pos), x, pos))
        heapq.heappush(self.q, (self.calc_dst(pos, y), pos, y))
        return pos

    def leave(self, p: int) -> None:
        head = tail = None
        for item in self.q:
            dst, x, y = item
            if y == p:
                head = item
            if x == p:
                tail = item
        if head:
            self.q.remove(head)
        if tail:
            self.q.remove(tail)
        
        heapq.heapify(self.q)

        if head and tail:
            heapq.heappush(self.q, (self.calc_dst(head[1], tail[2]), head[1], tail[2]))
        

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)