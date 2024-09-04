from typing import (
    List,
)

class SparseVector:
    # Your SparseVector object will be instantiated and called as such:
    # v1 = SparseVector(nums1)
    # v2 = SparseVector(nums2)
    # ans = v1.dot_product(v2)
    def __init__(self, nums: List[int]):
        # do intialization here
        self.nonzero = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.nonzero[i] = num

    # Return the dotProduct of two sparse vectors
    def dot_product(self, vec: "SparseVector") -> int:
        # write your code here
        
        res = 0 
        if len(self.nonzero) > len(vec.nonzero):
            for key, val in self.nonzero.items():
                if key in vec.nonzero:
                    res += (val * vec.nonzero[key])
        else:
            for key, val in vec.nonzero.items():
                if key in self.nonzero:
                    res += (val * self.nonzero[key])
        return res