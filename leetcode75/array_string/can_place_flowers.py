from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        N = len(flowerbed)
        cnt = 0
        for idx in range(0, N):
            if flowerbed[idx] == 1:
                continue
            else:
                if idx + 1 < N and flowerbed[idx + 1] == 1:
                    continue
                if idx - 1 >= 0 and flowerbed[idx - 1] == 1:
                    continue
                cnt += 1
                flowerbed[idx] = 1
                if cnt == n:
                    return True
        return False
