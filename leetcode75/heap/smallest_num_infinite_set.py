from heapq import heappop, heappush

class SmallestInfiniteSet:

    def __init__(self):
        self.h = [item for item in range(1, 1001)]

    def popSmallest(self) -> int:
        res = heappop(self.h)
        return res

    def addBack(self, num: int) -> None:
        if num in self.h:
            return
        heappush(self.h, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
