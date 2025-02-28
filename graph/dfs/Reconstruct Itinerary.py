from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_lst = defaultdict(list)
        used_edges = defaultdict(list)
        tickets.sort(key=lambda x: x[1])
        for fr, to in tickets:
            adj_lst[fr].append(to)
            used_edges[fr].append(False)

        def dfs(cur_node, lst):

            for idx in range(len(adj_lst[cur_node])):
                neighbor = adj_lst[cur_node][idx]
                if used_edges[cur_node][idx]:
                    continue
                used_edges[cur_node][idx] = True

                lst.append(neighbor)
                tmp = dfs(neighbor, lst)
                if tmp:
                    return tmp
                used_edges[cur_node][idx] = False
                lst.pop()

            if len(lst) == len(tickets):
                return lst

            return []

        lst = []
        return ["JFK"] + dfs("JFK", lst)


# OPTIMAL SOLUTIOn
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_lst = defaultdict(list)
        tickets.sort(key=lambda x: x[1], reverse=True)
        for fr, to in tickets:
            adj_lst[fr].append(to)

        route = []

        def dfs(cur_node):
            while adj_lst[cur_node]:
                next_airport = adj_lst[cur_node].pop()
                dfs(next_airport)
            route.append(cur_node)

        dfs("JFK")
        return route[::-1]
