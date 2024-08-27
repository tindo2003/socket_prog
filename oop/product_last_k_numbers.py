class ProductOfNumbers:

    def __init__(self):
        self.arr = []

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = []
        else:
            if self.arr:
                self.arr.append(num * self.arr[-1])
            else:
                self.arr.append(num)

    def getProduct(self, k: int) -> int:
        if len(self.arr) < k:
            return 0
        if len(self.arr) == k:
            return self.arr[-1]
        return self.arr[-1] // self.arr[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)