class ProductOfNumbers:

    def __init__(self):
        self.arr = []

    def add(self, num: int) -> None:
        if len(self.arr) == 0:
            self.arr.append(num)
        if num == 0:
            self.arr = [0]
        if self.arr[-1] == 0:
            # cancel out the 0
            self.arr = [num]
        else:
            self.arr.append(num * self.arr[-1])

    def getProduct(self, k: int) -> int:
        N = len(self.arr)
        if k > N:
            return 0
        if k == N:
            return self.arr[N - 1]
        else:
            return self.arr[-1] // self.arr[N - 1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
