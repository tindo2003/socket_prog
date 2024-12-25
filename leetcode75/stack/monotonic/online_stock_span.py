class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # the main idea is to remove all number less than or equal to cur num
        tmp = 1
        while self.stack:
            val, num_beated = self.stack[-1]
            if price >= val:
                self.stack.pop()
                tmp += num_beated
            else:
                break
        self.stack.append((price, tmp))
        return tmp


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
