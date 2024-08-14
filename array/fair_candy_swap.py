from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # exchange one candy box each
        # aSum - a + b = bSum - b + a
        # 2a = 2b + aSum - bSum
        # a = b + (aSum - bSum) / 2
        aSum = sum(aliceSizes)
        bSum = sum(bobSizes)
        delta = (aSum - bSum) // 2

        setA = set(aliceSizes)
        for b in bobSizes:
            if b + delta in setA:
                return [b + delta, b]

def main():
    sol = Solution()
    aliceSizes = [2]
    bobSizes = [1,3]
    res = sol.fairCandySwap(aliceSizes, bobSizes)
    print(res)

if __name__ == "__main__":
    main()