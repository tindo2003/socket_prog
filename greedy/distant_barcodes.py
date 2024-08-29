from typing import List 
from collections import Counter
import heapq 
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # the idea is to alternate even and odd indices
        counter = Counter(barcodes)
        h = []
        for key, val in counter.items():
            # max heap
            heapq.heappush(h, (-val, key))
        N = len(barcodes)
        res = [0] * N
        cur_idx = 0
        even = True 
        for val, key in h:
            freq = val * -1
            while freq > 0:
                # it is filled
                while res[cur_idx] != 0:
                    cur_idx += 2 
                    if cur_idx >= N:
                        if even:
                            cur_idx = 0
                        else:
                            cur_idx = 1
                        even = not even
                res[cur_idx] = key 
                freq -= 1
        return res 

def main():
    sol = Solution()
    barcodes = [1,1,1,1,2,2,3,3]
    res = sol.rearrangeBarcodes(barcodes)
    print(res)

if __name__ == "__main__":
    main()