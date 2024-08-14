
from typing import List 
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
      self.h = []
      self.k = k
      for num in nums:
        heapq.heappush(self.h, num)

        if len(self.h) > k:
          heapq.heappop(self.h) 

    def add(self, val: int) -> int:
      heapq.heappush(self.h, val)
      if len(self.h) > self.k:
        heapq.heappop(self.h)
      return self.h[0]

def main():
   obj = KthLargest(k=3, nums=[4, 5, 8, 2])


if __name__ == "__main__":
   main()