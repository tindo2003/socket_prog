class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Kahn's algorithm for Topological Sorting
        N = len(graph)
        out_degrees = [0] * N
        my_dict = defaultdict(list)

        for fr, lst in enumerate(graph):
            for to in lst:
                out_degrees[fr] += 1
                my_dict[to].append(fr)

        q = []
        res = set()
        for node, num in enumerate(out_degrees):
            if num == 0:
                q.append(node)
                res.add(node)
        while q:
            cur = q.pop(0)
            from_nodes = my_dict[cur]
            for fr in from_nodes:
                out_degrees[fr] -= 1
                if out_degrees[fr] == 0 and fr not in res:
                    res.add(fr)
                    q.append(fr)
        res = list(res)
        res.sort()
        return res
