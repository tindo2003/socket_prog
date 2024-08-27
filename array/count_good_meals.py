from typing import List
from collections import Counter
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        my_sum = 0 
        counter = Counter()
        for item in deliciousness:
            for i in range(22):
                cur_power_of_2 = 2**i 
                wanted_num = cur_power_of_2 - item
                if wanted_num in counter:
                    my_sum += counter[wanted_num]
            counter[item] += 1
        return my_sum


def main():
    sol = Solution()
    deliciousness = [1,3,5,7,9]
    res = sol.countPairs(deliciousness)
    print(res)

if __name__ == "__main__":
    main()
