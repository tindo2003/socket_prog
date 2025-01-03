from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        my_dict = {}
        l = 0
        res = 0
        N = len(fruits)
        for r in range(N):
            cur_fruit = fruits[r]
            if cur_fruit in my_dict:
                my_dict[cur_fruit] += 1
            else:
                my_dict[cur_fruit] = 1
            if len(my_dict.keys()) > 2:
                left_fruit = fruits[l]
                my_dict[left_fruit] -= 1
                if my_dict[left_fruit] == 0:
                    del my_dict[left_fruit]
                l += 1
            res = max(res, r - l + 1)
        return res
