from typing import (
    List,
)
from heapq import heappop, heappush
from math import inf


class Solution:
    """
    @param lights: Location and extent of illumination of street lights
    @return: The brightest position
    """

    def brightest_position(self, lights: List[List[int]]) -> int:
        maxi = -inf
        ans = -1
        num_on_lights = 0
        # write your code here
        h = []

        for pos, r in lights:
            # if start and end have the same value, we want start event to go in front of off event
            heappush(h, (pos - r, 0))
            heappush(h, (pos + r, 1))

        while h:
            val, status = heappop(h)
            if status == 0:
                num_on_lights += 1
                if num_on_lights > maxi:
                    maxi = num_on_lights
                    ans = val
            else:
                num_on_lights -= 1
        return ans


def main():
    sol = Solution()
    res = sol.brightest_position([[1, 0], [0, 1]])
    print(res)


if __name__ == "__main__":
    main()
