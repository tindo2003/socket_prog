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
            stops = [inf] * n
            dist[src] = 0
            stops[src] = 0
            w = defaultdict(int)
            adj_lst = defaultdict(list)

            for x, y, weight in flights:
                adj_lst[x].append(y)
                w[(x, y)] = weight

            h = [(0, src, 0)]

            while h:
                cur_dist, cur, cur_stop = heappop(h)

                if cur == dst:
                    return cur_dist

                if cur_stop > k:
                    continue

                new_stop = cur_stop + 1
                for neighbor in adj_lst[cur]:
                    new_dist = cur_dist + w[(cur, neighbor)]
                    if new_dist < dist[neighbor] or new_stop < stops[neighbor]:
                        dist[neighbor] = new_dist
                        stops[neighbor] = new_stop
                        heappush(h, (new_dist, neighbor, new_stop))

            return -1

        return dijkstra()
