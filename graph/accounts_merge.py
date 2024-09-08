from typing import List 
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Two accounts definitely belong to the same person if there is some common email to both accounts.
        # pretend each string is a separate node. find connected components.
        # the idea is to store note at the beginning of each node
        adj_lst = defaultdict(list)
        for emails in accounts:
            N = len(emails)
            for i in range(1, N):
                if emails[i] not in adj_lst:
                    adj_lst[emails[i]] = [emails[0]]
                for j in range(i + 1, N):
                    adj_lst[emails[i]].append(emails[j])
                    if emails[j] not in adj_lst:
                        adj_lst[emails[j]] = [emails[0]]
                    adj_lst[emails[j]].append(emails[i])
        visited = set()
        def dfs(cur, component):
            component.append(cur)
            for neighbor in adj_lst[cur][1:]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, component)
        res = []
        for node in adj_lst.keys():
            if node not in visited:
                visited.add(node)
                tmp = []
                dfs(node, tmp)
                res.append(tmp)
        final_res = []
        for item in res:
            item.sort()
            new_item = [adj_lst[item[0]][0]] + item
            final_res.append(new_item)
        return final_res        
