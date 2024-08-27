from collections import heapq
class StockPrice:

    def __init__(self):
        self.stocks = {}
        self.min_heap = []
        self.max_heap = []
        self.latest_time = -1 

    def update(self, timestamp: int, price: int) -> None:
        self.stocks[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.stocks[self.latest_time]

    def maximum(self) -> int:
        while -self.max_heap[0][0] != self.stocks[self.max_heap[0][1]]:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0][0]

    def minimum(self) -> int:
        while self.min_heap[0][0] != self.stocks[self.min_heap[0][1]]:
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]


