from typing import List
from collections import defaultdict
from math import inf
from heapq import heappush, heappop


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        def dijkstra():
            dist = [inf] * n
            dist[src] = 0
            w = defaultdict(int)
            adj_lst = defaultdict(list)

            for x, y, weight in flights:
                adj_lst[x].append(y)
                w[(x, y)] = weight

            h = [(0, src)]

            while h:
                cur_dist, cur = heappop(h)
                if cur == dst:
                    return cur_dist

                # stale
                if cur_dist != dist[cur]:  # keep track of visited
                    continue

                for neighbor in adj_lst[cur]:
                    new_dist = cur_dist + w[(cur, neighbor)]
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        heappush(h, (new_dist, neighbor))

            return -1

        return dijkstra()
