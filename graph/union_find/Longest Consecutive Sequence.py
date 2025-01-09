from typing import List
from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        N = len(nums)
        parents = [i for i in range(N)]
        rank = {i: 0 for i in range(N)}
        my_dict = {nums[idx]: idx for idx in range(N)}

        def union(child, parent):
            child_root = find(child)
            parent_root = find(parent)
            if child_root == parent_root:
                return
            # Union by Rank: Attach smaller rank tree under the larger rank tree
            if rank[child_root] > rank[parent_root]:
                parents[parent_root] = child_root
            elif rank[child_root] < rank[parent_root]:
                parents[child_root] = parent_root
            else:
                # If ranks are equal, attach one under the other and increase the rank
                parents[child_root] = parent_root
                rank[parent_root] += 1

        def find(cur):
            if parents[cur] != cur:
                parents[cur] = find(parents[cur])  # Path compression
            return parents[cur]

        for idx, num in enumerate(nums):
            if num - 1 in my_dict:
                union(idx, my_dict[num - 1])
            if num + 1 in my_dict:
                union(idx, my_dict[num + 1])

        group_sizes = defaultdict(int)
        for i in range(N):
            root = find(i)
            group_sizes[root] += 1

        return max(group_sizes.values(), default=0)
