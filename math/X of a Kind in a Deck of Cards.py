from typing import List
from collections import Counter
import math


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = Counter(deck)
        values = list(freq.values())

        def gcd_of_list(numbers):
            result = numbers[0]
            for num in numbers[1:]:
                result = math.gcd(result, num)
            return result

        return gcd_of_list(values) > 1
