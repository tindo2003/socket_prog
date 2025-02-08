from collections import defaultdict
from sortedcontainers import SortedSet


class NumberContainers:

    def __init__(self):
        self.number_to_idx = defaultdict(SortedSet)
        self.idx_to_number = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        ordered_set = self.number_to_idx[number]
        ordered_set.add(index)
        if index in self.idx_to_number:
            last_owner = self.idx_to_number[index]
            if last_owner != number:
                self.number_to_idx[last_owner].remove(index)
        self.idx_to_number[index] = number

    def find(self, number: int) -> int:
        if number not in self.number_to_idx or len(self.number_to_idx[number]) == 0:
            return -1
        return self.number_to_idx[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
