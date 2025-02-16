from typing import List
from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls_to_colors = defaultdict(int)
        colors_freq = defaultdict(int)
        res = []
        for x, y in queries:
            if x in balls_to_colors:
                prev_color = balls_to_colors[x]
                colors_freq[prev_color] -= 1
                if colors_freq[prev_color] == 0:
                    del colors_freq[prev_color]
            colors_freq[y] += 1
            balls_to_colors[x] = y
            res.append(len(colors_freq))
        return res
